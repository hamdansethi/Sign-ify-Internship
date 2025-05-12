from llama_index.utils.workflow import draw_all_possible_flows
from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
)


class MyWorkflow(Workflow):
    @step
    async def my_step(self, ev: StartEvent) -> StopEvent:
        # do something here
        return StopEvent(result="Hello, world!")

draw_all_possible_flows(MyWorkflow, filename="basic_workflow.html")