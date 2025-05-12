from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
    Event,
    Context,
)
from llama_index.utils.workflow import draw_all_possible_flows
import asyncio


class Step2Event(Event):
    query: str


class DefaultSubflow(Workflow):
    @step()
    async def sub_start(self, ctx: Context, ev: StartEvent) -> StopEvent:
        print("Doing basic reflection")
        return StopEvent(result="Improved query")

class MainWorkflow(Workflow):
    @step
    async def start(
        self, ctx: Context, ev: StartEvent, reflection_workflow: Workflow
    ) -> Step2Event:
        print("Need to run reflection")
        res = await reflection_workflow.run(query=ev.query)

        return Step2Event(query=res)

    @step
    async def step_two(self, ctx: Context, ev: Step2Event) -> StopEvent:
        print("Query is ", ev.query)
        # do something with the query here
        return StopEvent(result=ev.query)
    
    @step()
    async def start(
        self,
        ctx: Context,
        ev: StartEvent,
        reflection_workflow: Workflow = DefaultSubflow(),
    ) -> Step2Event:
        print("Need to run reflection")
        res = await reflection_workflow.run(query=ev.query)

        return Step2Event(query=res)



    



class ReflectionFlow(Workflow):
    @step
    async def sub_start(self, ctx: Context, ev: StartEvent) -> StopEvent:
        print("Doing custom reflection")
        return StopEvent(result="Improved query")
    

    

async def main():
    w = MainWorkflow(timeout=10, verbose=False)
    w.add_workflows(reflection_workflow=ReflectionFlow())
    result = await w.run(query="Initial query")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())