from typing import Optional, List


from dataclasses import dataclass


@dataclass
class Task:
  name: str
  cmd: Optional[str]
  description: Optional[str]
  depends_on: List[str]
  cwd: None
  env: None
  clean_env: bool
  inputs: Optional[List[str]]
  outputs: Optional[List[str]]


@dataclass
class Feature:
  name: str
  tasks: List[Task]


@dataclass
class TaskInfo:
  environment: str
  features: List[Feature]
