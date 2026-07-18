import { ToolDecorator as Tool, ExecutionContext, z } from '@nitrostack/core';

export class ViyanTools {

  @Tool({
    name: "run_simulation",
    description: "Run the complete Viyan satellite collision simulation.",
    inputSchema: z.object({})
  })
  async runSimulation(_: any, ctx: ExecutionContext) {

    ctx.logger.info("Running Viyan simulation");

    const response = await fetch(
      "http://127.0.0.1:8000/api/v1/simulation/run",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        }
      }
    );

    if (!response.ok) {
      throw new Error(`Backend returned ${response.status}`);
    }

    return await response.json();
  }

  @Tool({
    name: "get_satellites",
    description: "Retrieve all tracked satellites.",
    inputSchema: z.object({})
  })
  async getSatellites(_: any, ctx: ExecutionContext) {

    ctx.logger.info("Fetching satellites");

    const response = await fetch(
      "http://127.0.0.1:8000/api/v1/simulation/satellites"
    );

    if (!response.ok) {
      throw new Error(`Backend returned ${response.status}`);
    }

    return await response.json();
  }

  @Tool({
    name: "get_conjunctions",
    description: "Retrieve detected satellite conjunctions.",
    inputSchema: z.object({})
  })
  async getConjunctions(_: any, ctx: ExecutionContext) {

    ctx.logger.info("Fetching conjunctions");

    const response = await fetch(
      "http://127.0.0.1:8000/api/v1/simulation/conjunctions"
    );

    if (!response.ok) {
      throw new Error(`Backend returned ${response.status}`);
    }

    return await response.json();
  }

  @Tool({
    name: "assess_risk",
    description: "Assess collision risk for detected conjunctions.",
    inputSchema: z.object({})
  })
  async assessRisk(_: any, ctx: ExecutionContext) {

    ctx.logger.info("Assessing collision risk");

    const response = await fetch(
      "http://127.0.0.1:8000/api/v1/simulation/risk"
    );

    if (!response.ok) {
      throw new Error(`Backend returned ${response.status}`);
    }

    return await response.json();
  }

  @Tool({
    name: "predict_collision",
    description: "Predict collision probability using the ML model.",
    inputSchema: z.object({})
  })
  async predictCollision(_: any, ctx: ExecutionContext) {

    ctx.logger.info("Predicting collision probability");

    const response = await fetch(
      "http://127.0.0.1:8000/api/v1/simulation/prediction"
    );

    if (!response.ok) {
      throw new Error(`Backend returned ${response.status}`);
    }

    return await response.json();
  }

  @Tool({
    name: "negotiate",
    description: "Generate an autonomous collision avoidance recommendation.",
    inputSchema: z.object({})
  })
  async negotiate(_: any, ctx: ExecutionContext) {

    ctx.logger.info("Generating avoidance maneuver");

    const response = await fetch(
      "http://127.0.0.1:8000/api/v1/simulation/negotiation"
    );

    if (!response.ok) {
      throw new Error(`Backend returned ${response.status}`);
    }

    return await response.json();
  }

  @Tool({
    name: "get_satellite_status",
    description: "Get the real-time position, velocity, and geographic location of a satellite.",
    inputSchema: z.object({
      name: z.string().describe("Satellite name (e.g. ISS or SOYUZ)")
    })
  })
  async getSatelliteStatus(
    input: { name: string },
    ctx: ExecutionContext
  ) {

    ctx.logger.info(`Fetching status for ${input.name}`);

    const response = await fetch(
      `http://127.0.0.1:8000/api/v1/simulation/satellite/${encodeURIComponent(input.name)}`
    );

    if (!response.ok) {
      throw new Error(`Backend returned ${response.status}`);
    }

    return await response.json();
  }

}