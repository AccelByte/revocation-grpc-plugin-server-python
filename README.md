# revocation_server_python

```mermaid
flowchart LR
   subgraph AccelByte Gaming Services
   CL[gRPC Client]
   end
   subgraph gRPC Server Deployment
   SV["gRPC Server\n(YOU ARE HERE)"]
   DS[Dependency Services]
   CL --- DS
   end
   DS --- SV
```

`AccelByte Gaming Services` capabilities can be extended using custom functions implemented in a `gRPC server`. If configured, custom functions in the `gRPC server` will be called by `AccelByte Gaming Services` instead of the default function.

The `gRPC server` and the `gRPC client` can actually communicate directly. However, additional services are necessary to provide **security**, **reliability**, **scalability**, and **observability**. We call these services as `dependency services`. The [grpc-plugin-dependencies](https://github.com/AccelByte/grpc-plugin-dependencies) repository is provided as an example of what these `dependency services` may look like. It
contains a docker compose which consists of these `dependency services`.

> :warning: **grpc-plugin-dependencies is provided as example for local development purpose only:** The dependency services in the actual gRPC server deployment may not be exactly the same.

## Overview

This repository contains a `revocation gRPC server app` written in `python`. It provides a simple custom rotating shop items function for platform service in `AccelByte Gaming Services`.

This sample app also shows how this `gRPC server` can be instrumented for better observability. 
It is configured by default to send metrics, traces, and logs to the observability `dependency services` in [grpc-plugin-dependencies](https://github.com/AccelByte/grpc-plugin-dependencies).

## Prerequisites

1. Windows 10 WSL2 or Linux Ubuntu 20.04 with the following tools installed.

   a. bash

   b. make

   c. docker v23.x

   d. docker-compose v2.x

   e. docker loki driver
        
      ```
      docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions
      ```

    f. python 3.9

    g. git

    h. [ngrok](https://ngrok.com/)

    i. [postman](https://www.postman.com/)

2. A local copy of [grpc-plugin-dependencies](https://github.com/AccelByte/grpc-plugin-dependencies) repository.

   ```
   git clone https://github.com/AccelByte/grpc-plugin-dependencies.git
   ```

3. Access to `AccelByte Gaming Services` demo environment.

    a. Base URL: https://demo.accelbyte.io.

    b. [Create a Game Namespace](https://docs.accelbyte.io/esg/uam/namespaces.html#tutorials) if you don't have one yet. Keep the `Namespace ID`.

    c. [Create an OAuth Client](https://docs.accelbyte.io/guides/access/iam-client.html) with `confidential` client type. Keep the `Client ID` and `Client Secret`.

## Setup

To be able to run this sample app, you will need to follow these setup steps.

1. Create a docker compose `.env` file by copying the content of [.env.template](.env.template) file.

   > :warning: **The host OS environment variables have higher precedence compared to `.env` file variables**: If the variables in `.env` file do not seem to take effect properly, check if there are host OS environment variables with the same name. 
   See documentation about [docker compose environment variables precedence](https://docs.docker.com/compose/environment-variables/envvars-precedence/) for more details.

2. Fill in the required environment variables in `.env` file as shown below.

   ```
   AB_BASE_URL=https://demo.accelbyte.io      # Base URL of AccelByte Gaming Services demo environment
   AB_CLIENT_ID='xxxxxxxxxx'                  # Use Client ID from the Prerequisites section
   AB_CLIENT_SECRET='xxxxxxxxxx'              # Use Client Secret from the Prerequisites section
   AB_NAMESPACE='xxxxxxxxxx'                  # Use Namespace ID from the Prerequisites section
   PLUGIN_GRPC_SERVER_AUTH_ENABLED=false      # Enable or disable access token and permission verification
   ```

   > :warning: **Keep PLUGIN_GRPC_SERVER_AUTH_ENABLED=false for now**: It is currently not
   supported by `AccelByte Gaming Services` but it will be enabled later on to improve security. If it is
   enabled, the gRPC server will reject any calls from gRPC clients without proper authorization
   metadata.

## Building

To build this sample app, use the following command.

```
make build
```

## Running

To (build and) run this sample app in a container, use the following command.

```
docker-compose up --build
```

## Testing

### Functional Test in Local Development Environment

The custom functions in this sample app can be tested locally using `postman`.

1. Run the `dependency services` by following the `README.md` in the [grpc-plugin-dependencies](https://github.com/AccelByte/grpc-plugin-dependencies) repository.

   > :warning: **Make sure to start dependency services with mTLS disabled for now**: It is currently not supported by `AccelByte Gaming Services` but it will be enabled later on to improve security. If it is enabled, the gRPC client calls without mTLS will be rejected.

2. Run this `gRPC server` sample app.

3. Open `postman`, create a new `gRPC request`, and enter `localhost:10000` as server URL. 

   > :exclamation: We are essentially accessing the `gRPC server` through an `Envoy` proxy in `dependency services`.

4. Still in `postman`, continue by selecting `Revocation/Revoke` method and invoke it with the sample message below.

   ```json
   {
       "revokeEntryType": "CURRENCY",
       "namespace": "test",
       "userId": "4423f033c38a40b9afdc8844e13647b7",
       "quantity": 1,
       "currency": {
           "namespace": "test",
           "currencyCode": "VCA",
           "balanceOrigin": "SYSTEM"
       }
   }
   ```

5. If successful, you will see the item(s) in the response.

   ```json
   {
        "customRevocation": [
            {
                "key": "currencyNamespace",
                "value": "test"
            },
            {
                "key": "quantity",
                "value": "1"
            },
            {
                "key": "namespace",
                "value": "test"
            },
            {
                "key": "userId",
                "value": "4423f033c38a40b9afdc8844e13647b7"
            },
            {
                "key": "currencyCode",
                "value": "VCA"
            },
            {
                "key": "balanceOrigin",
                "value": "SYSTEM"
            }
        ],
        "status": "SUCCESS",
        "reason": ""
    }
    ```

### Integration Test with AccelByte Gaming Services

After passing functional test in local development environment, you may want to perform
integration test with `AccelByte Gaming Services`. Here, we are going to expose the `gRPC server`
in local development environment to the internet so that it can be called by
`AccelByte Gaming Services`. To do this without requiring public IP, we can use [ngrok](https://ngrok.com/)

1. Run the `dependency services` by following the `README.md` in the [grpc-plugin-dependencies](https://github.com/AccelByte/grpc-plugin-dependencies) repository.

   > :warning: **Make sure to start dependency services with mTLS disabled for now**: It is currently not supported by `AccelByte Gaming Services`, but it will be enabled later on to improve security. If it is enabled, the gRPC client calls without mTLS will be rejected.

2. Run this `gRPC server` sample app.

3. Sign-in/sign-up to [ngrok](https://ngrok.com/) and get your auth token in `ngrok` dashboard.

4. In [grpc-plugin-dependencies](https://github.com/AccelByte/grpc-plugin-dependencies) repository folder, run the following command to expose the `Envoy` proxy port connected to the `gRPC server` in local development environment to the internet. Take a note of the `ngrok` forwarding URL e.g. `tcp://0.tcp.ap.ngrok.io:xxxxx`.

   ```
   make ngrok NGROK_AUTHTOKEN=xxxxxxxxxxx    # Use your ngrok auth token
   ```

5. [Create an OAuth Client](https://docs.accelbyte.io/guides/access/iam-client.html) with `confidential` client type with the following permissions.  Keep the `Client ID` and `Client Secret`. This is different from the Oauth Client from the Prerequisites section and it is required by CLI demo app [here](demo/cli/) in the next step to register the `gRPC Server` URL.

   - ADMIN:NAMESPACE:{namespace}:PLUGIN:REVOCATION [UPDATE, DELETE]
   - ADMIN:NAMESPACE:{namespace}:REVOCATION [UPDATE]
   - ADMIN:NAMESPACE:{namespace}:USER:*:REVOCATION [UPDATE]
   - ADMIN:NAMESPACE:{namespace}:STORE [READ, CREATE, UPDATE, DELETE]
   - ADMIN:NAMESPACE:{namespace}:CATEGORY [CREATE]
   - ADMIN:NAMESPACE:{namespace}:ITEM [CREATE, DELETE]
   - ADMIN:NAMESPACE:{namespace}:CURRENCY [CREATE, DELETE]

   > :warning: **Oauth Client created in this step is different from the one from Prerequisites section:** It is required by CLI demo app [here](demo/cli/) in the next step to register the `gRPC Server` URL.

6. Create a user for testing. Keep the `Username` and `Password`.

7. Create a `.env` file by copying the content of [.env.example](demo/cli/.env.example) and set the necessary environment variables then run the [Makefile](Makefile) CLI command. The CLI will set up the necessary configuration and then give you instructions on how to configure platform service. If successful, the word `[SUCCESS]` will be print out in the terminal.

   ```
   AB_BASE_URL='https://demo.accelbyte.io'
   AB_CLIENT_ID='xxxxxxxxxx'       # Use Client ID from the previous step
   AB_CLIENT_SECRET='xxxxxxxxxx'   # Use Client secret from the previous step
   AB_NAMESPACE='xxxxxxxxxx'       # Use your Namespace ID
   AB_USERNAME='xxxxxxxxxx'       # Use your Namespace Username
   AB_PASSWORD='xxxxxxxxxx'       # Use your Namespace Password
   GRPC_SERVER_URL='0.tcp.ap.ngrok.io:xxxxx'   # Use your ngrok forwarding URL
   ```
   then run in the terminal
   ```
   $ cd demo/cli
   $ make setup
   $ make run
   ```

> :warning: **Ngrok free plan has some limitations**: You may want to use paid plan if the traffic is high.

## Pushing

To build and push this sample app multi-arch container image to AWS ECR, use the following command.

```
make imagex_push REPO_URL=xxxxxxxxxx.dkr.ecr.us-west-2.amazonaws.com/accelbyte/justice/development/extend/xxxxxxxxxx/xxxxxxxxxx IMAGE_TAG=v0.0.1
```
