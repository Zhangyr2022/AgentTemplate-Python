import asyncio

import novelcraft.sdk as sdk


async def main():
    await sdk.initialize()
    sdk.get_logger().info('Hello, world!')

    while True:
        # Required to keep the SDK alive
        await asyncio.sleep(0.1)

        agent = sdk.get_agent()

        if agent is None:
            continue

        agent.set_movement(sdk.IAgent.MovementKind.FORWARD)

    await ncsdk.finalize()
    ncsdk.get_logger().info('Goodbye, world!')

if __name__ == '__main__':
    asyncio.run(main())
