# Docker ECS Feature List
| Features | Current | Edge/GA | 
| ----------- | ----------- | -----------
| Secrets | :heavy_check_mark: | :heavy_check_mark: |
| IAM roles | | :heavy_check_mark: |
| env file | | :heavy_check_mark: |
| Rolling update | | :heavy_check_mark: |
| ECR Support  | :heavy_check_mark: | :heavy_check_mark: |

-----------

# Docker ECS Plugin Command Diff
| Command | Current | Edge/GA |
| ----------- | ----------- | -----------
| setup | `docker ecs setup` | `docker context create` |
| up | `docker ecs compose up` | `docker compose up` |
| down | `docker ecs compose down` | `docker compose down` |
| ps | `docker ecs compose ps`  | `docker compose ps` |
| logs | `docker ecs compose logs`  | `docker compose logs`|
| convert | `docker ecs compose convert` | `docker compose convert`|
