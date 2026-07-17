import { PromptDecorator as Prompt, ExecutionContext } from '@nitrostack/core';

export class ViyanPrompts {

  @Prompt({
    name: 'analyze_collision_risk',
    description: 'Generate guidance for analyzing satellite collision risk.',
    arguments: [
      {
        name: 'satellite',
        description: 'Optional satellite name or NORAD ID',
        required: false
      }
    ]
  })
  async analyzeCollisionRisk(args: any, ctx: ExecutionContext) {

    ctx.logger.info('Generating collision risk prompt');

    const satellite = args?.satellite;

    if (satellite) {
      return [
        {
          role: 'user' as const,
          content: `Analyze the collision risk for satellite "${satellite}".`
        },
        {
          role: 'assistant' as const,
          content:
            `Use the VIYAN MCP tools to:
1. Retrieve conjunction information.
2. Assess the collision risk.
3. Predict collision probability using the ML model.
4. Recommend an avoidance maneuver if required.`
        }
      ];
    }

    return [
      {
        role: 'user' as const,
        content: 'Analyze the latest satellite conjunctions.'
      },
      {
        role: 'assistant' as const,
        content:
`Use the VIYAN MCP tools in this order:

1. run_simulation
2. get_conjunctions
3. assess_risk
4. predict_collision
5. negotiate

Summarize:
- Number of conjunctions detected
- Collision probability
- Risk level
- Recommended maneuver
- Overall mission impact`
      }
    ];
  }


  @Prompt({
    name: 'simulation_summary',
    description: 'Summarize the latest simulation results.',
    arguments: []
  })
  async simulationSummary(_: any, ctx: ExecutionContext) {

    ctx.logger.info('Generating simulation summary prompt');

    return [
      {
        role: 'user' as const,
        content: 'Summarize the latest VIYAN simulation.'
      },
      {
        role: 'assistant' as const,
        content:
`Run the simulation and produce a concise report including:

- Satellites analyzed
- Conjunctions detected
- Highest collision probability
- Risk assessment
- Recommended avoidance maneuver
- Final mission status`
      }
    ];
  }
}