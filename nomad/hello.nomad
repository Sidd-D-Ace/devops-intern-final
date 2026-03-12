job "hello-devops" {
  datacenters = ["dc1"]
  type = "batch"

  group "python-group" {
    count = 1

    task "python-task" {
      driver = "docker"

      config {
        image = "python:3.9-slim"
        command = "python"
        args = ["-c", "print('Hello, DevOps! Running inside Nomad.')"]
      }

      resources {
        cpu    = 100 
        memory = 128
      }
    }
  }
}