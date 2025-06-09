# Opentelemetry Traces, Spans and Events via. Python

This repository has examples implementing traces, spans and event analytics via. Opentelemetry in Python. An example of visualizing these via. Jaeger (running on docker) is also provided. 

## What are Traces, Spans, Events ...

The major components of trace analytics via. Opentelemetry are as follows

* **Trace** is the overall view of a request's journey <br>
* **Span(s)** are individual operations or units of work within that journey <br>
* **Event(s)** are discrete points of interest within a span

For example, if you had a button on a website that submitted an order, loaded a new web page with a confirmation and sent a confirmation email, each click of the button could be a trace ie. the order trace. Under each order trace could would be multiple spans. The first span for writing the order information to a database, the second for the be the GET request and loading of the confirmation page and a third span for sending the confirmation email.

Structuring the trace and spans like ^ would give you a nice graph showing how long the overall process (trace) took and how long each of the subprocess (span) took. 

If you had issues with this process would could look a visual of the traces and/or spans to see where a process failed or incurred additional latency.

Additionally at any point in a span we can also record an event which would be a discrete point of interest.

## Python Code Examples 



## Visualizing Traces, Spans, Events via. Jaeger

