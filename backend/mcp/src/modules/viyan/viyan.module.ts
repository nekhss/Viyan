import { Module } from '@nitrostack/core';
import { ViyanTools } from './viyan.tools.js';
import { ViyanResources } from './viyan.resources.js';
import { ViyanPrompts } from './viyan.prompts.js';

@Module({
  name: 'viyan',
  description: 'VIYAN Space Traffic Management MCP',
  controllers: [ViyanTools, ViyanResources, ViyanPrompts]
})
export class ViyanModule {}