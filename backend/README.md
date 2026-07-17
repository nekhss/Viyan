# 🚀 VIYAN - AI-Powered Space Traffic Management MCP Server

VIYAN is an AI-powered Space Traffic Management platform that helps detect potential satellite collisions, assess collision risk, predict collision probability using Machine Learning, and recommend autonomous collision avoidance maneuvers.

This project was built using the **NitroStack MCP Framework** for the MCP Hackathon.

---

# Features

- 🛰️ Track active satellites
- ☄️ Detect future satellite conjunctions
- ⚠️ Assess collision risk
- 🤖 Predict collision probability using Machine Learning
- 🛡️ Generate autonomous collision avoidance recommendations
- 🔌 Expose all capabilities through a Model Context Protocol (MCP) server

---

# Tech Stack

## Backend

- Python
- FastAPI
- Skyfield
- NumPy
- Pandas
- Scikit-learn

## MCP Server

- NitroStack SDK
- TypeScript
- Node.js

---

# Architecture

```
               AI Assistant
                     │
                     ▼
          NitroStack MCP Server
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 Simulation      Risk Analysis   ML Prediction
                     │
                     ▼
             FastAPI Backend
                     │
                     ▼
          Satellite Simulation Engine
```

---

# MCP Tools

The MCP server exposes the following tools:

| Tool | Description |
|------|-------------|
| run_simulation | Execute the complete collision simulation |
| get_satellites | Retrieve tracked satellites |
| get_conjunctions | Detect satellite conjunctions |
| assess_risk | Assess collision risk |
| predict_collision | Predict collision probability |
| negotiate | Recommend an avoidance maneuver |

---

# MCP Resources

- Simulation Status
- Tracked Satellites
- Latest Conjunction Report

---

# MCP Prompts

- Analyze Collision Risk
- Simulation Summary

---

# API Endpoints

| Method | Endpoint |
|---------|----------|
| POST | /api/v1/simulation/run |
| GET | /api/v1/simulation/satellites |
| GET | /api/v1/simulation/conjunctions |
| GET | /api/v1/simulation/risk |
| GET | /api/v1/simulation/prediction |
| GET | /api/v1/simulation/negotiation |

---

# Running the Backend

```bash
cd backend
uvicorn app.main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# Running the MCP Server

```bash
cd backend/mcp
npm install
npm run dev
```

Production build

```bash
npm run build
```

---

# Project Structure

```
backend/
│
├── app/
│   ├── api/
│   └── core/
│
├── simulation/
│   ├── collision.py
│   ├── risk.py
│   ├── negotiation.py
│   ├── features.py
│   ├── trajectory.py
│   └── ml/
│
└── mcp/
    ├── src/
    │   └── modules/
    │       └── viyan/
    │           ├── viyan.tools.ts
    │           ├── viyan.resources.ts
    │           ├── viyan.prompts.ts
    │           └── viyan.module.ts
```

---

# Future Improvements

- Multi-satellite negotiation
- Live orbital data streaming
- Real-time conjunction alerts
- Interactive dashboard
- LLM-assisted mission planning

---

# License

MIT