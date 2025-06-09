# OpenTelem trace code ...
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource

import time

# Add resource information with customer attributes ie. key value pair. These will be added to every span
resource = Resource(attributes={"service.name": "example-service"})

# Set up trace procider
provider = TracerProvider(resource=resource)

# Export spans to local Jaeger via OTLP/gRPC
otlp_exporter = OTLPSpanExporter(endpoint="localhost:4317", insecure=True)
processor = BatchSpanProcessor(otlp_exporter)

# Optional - Send the traces to the console
# processor = BatchSpanProcessor(ConsoleSpanExporter())

provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Define the trace for the add function
add_function_trace = trace.get_tracer("add-function-trace")

#
# Option 1 - Automatically add span(s) when a function is called
#

@add_function_trace.start_as_current_span("automatic-child-span-1-add-function") # Everytime the add function is called a span will automaticlly be added to the trace
def add(first, second): # Simple example function adding two numbers    
    
    current_span = trace.get_current_span() # Optional - Customize the current span
    current_span.set_status(trace.StatusCode.OK) # Optional - Set status OK or ERROR

    # Optional - Add an event
    print(first)
    current_span.add_event(name="print first number", attributes={"first_number": first}, timestamp = time.time_ns())
    time.sleep(1)

    return first + second

# Invoke ^ function
'''
return_val = add(1 , 2)
print(f"The result is: {return_val}")
'''

#
# Option 2 - Manually manipulate the spans
# 

# Create a root span
with add_function_trace.start_as_current_span("manual-root-trace") as root_span:
    
    # Create child span under root
    with add_function_trace.start_as_current_span("manual-child-span-1") as child_span_1:
        time.sleep(0.5)

        # Optional - Add you additonal code HERE

        child_span_1.add_event("Some event in child span 1 ...") # Optional - Add an event
        child_span_1.set_attribute("custom", "attribute 1") # Optinal - Set custom attribute
        child_span_1.set_status(trace.StatusCode.OK) # Optional - Set status OK

    # Create another child span under root
    with add_function_trace.start_as_current_span("manual-child-span-2") as child_span_2:
        time.sleep(0.8)
        
        # Optional - Add you additonal code HERE

        child_span_2.add_event("Some event in child span 2 ...") # Optional - Add an event
        child_span_2.set_attribute("custom", "attribute 2") # Optinal - Set custom attribute
        child_span_2.set_status(trace.StatusCode.ERROR) # Optional - Set status ERROR
