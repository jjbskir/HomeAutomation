from HomeAutomation.models import Lamp
from HomeAutomation.forms import ButtonForm
from HomeAutomation.serializers import LampSerializer
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import link, action
from rest_framework import status
from django.shortcuts import redirect

class LampViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Lamp.objects.all()
    serializer_class = LampSerializer
    
    @link(renderer_classes=[renderers.TemplateHTMLRenderer])
    def button(self, request, *args, **kwargs):
        '''
        Form for turning on and off the light.
        '''
        lamp = self.get_object()
        # What the button should say in the submit form.
        if lamp.state == 0:
            button = 'Turn On'
        else:
            button = 'Turn Off'
        form = ButtonForm
        return Response({'lamp': lamp, 'form': form, 'button': button}, template_name='button.html')
    
    @action(methods=['POST', 'PUT'])
    def buttonProcess(self, request, *args, **kwargs):
        '''
        How to process the form from button(). Turn on or off the lamp.
        '''
        lamp = self.get_object()
        serializer = LampSerializer(data=request.DATA)
        if serializer.is_valid():
            # change the lamp state.
            if lamp.state == 0:
                lamp.state = 1
            elif lamp.state == 1:
                lamp.state = 0
            lamp.save()
            # redirect back to button() if all goes correct.
            return redirect('/homeautomation/' + str(lamp.id) + '/button/')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @link(renderer_classes=[renderers.XMLRenderer])
    def xml(self, request, *args, **kwargs):
        '''
        XML output for viewing with arduino.
        '''
        lamp = self.get_object()
        content = {'state': lamp.state, 'name': lamp.name, 'date': lamp.date}
        return Response(content)
    