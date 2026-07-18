import { ResourceDecorator as Resource, ExecutionContext } from '@nitrostack/core';

export class ViyanResources {

  @Resource({
    uri: 'viyan://status',
    name: 'Simulation Status',
    description: 'Current status of the VIYAN simulation.',
    mimeType: 'application/json'
  })
  async simulationStatus(uri: string, ctx: ExecutionContext) {

    ctx.logger.info('Fetching simulation status');

    const response = await fetch(
      'http://127.0.0.1:8000/api/v1/simulation/conjunctions'
    );

    if (!response.ok) {
      throw new Error(`Backend returned ${response.status}`);
    }

    const data = await response.json() as {
      count: number;
    };

    return {
      contents: [
        {
          uri,
          mimeType: 'application/json',
          text: JSON.stringify(
            {
              status: 'online',
              total_conjunctions: data.count,
              generated_at: new Date().toISOString()
            },
            null,
            2
          )
        }
      ]
    };
  }

  @Resource({
    uri: 'viyan://satellites',
    name: 'Tracked Satellites',
    description: 'Currently tracked satellites.',
    mimeType: 'application/json'
  })
  async satellites(uri: string, ctx: ExecutionContext) {

    ctx.logger.info('Fetching satellites');

    const response = await fetch(
      'http://127.0.0.1:8000/api/v1/simulation/satellites'
    );

    if (!response.ok) {
      throw new Error(`Backend returned ${response.status}`);
    }

    const data = await response.json();

    return {
      contents: [
        {
          uri,
          mimeType: 'application/json',
          text: JSON.stringify(data, null, 2)
        }
      ]
    };
  }

  @Resource({
    uri: 'viyan://conjunctions',
    name: 'Detected Conjunctions',
    description: 'Latest detected conjunctions.',
    mimeType: 'application/json'
  })
  async conjunctions(uri: string, ctx: ExecutionContext) {

    ctx.logger.info('Fetching conjunctions');

    const response = await fetch(
      'http://127.0.0.1:8000/api/v1/simulation/conjunctions'
    );

    if (!response.ok) {
      throw new Error(`Backend returned ${response.status}`);
    }

    const data = await response.json();

    return {
      contents: [
        {
          uri,
          mimeType: 'application/json',
          text: JSON.stringify(data, null, 2)
        }
      ]
    };
  }

}