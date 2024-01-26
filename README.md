# Next Word Prediction using LLM inside AWS Lambda

## Description
This project focuses on Next Word Prediction using LLM, LangChain, GPT4ALL and containers.

## Requirements
* [LangChain](https://www.langchain.com/)
* [GPT4ALL](https://gpt4all.io/index.html)
* [Python Container Image](https://hub.docker.com/_/python)

## Local Deployment
1. Download a [GPT4ALL model](https://gpt4all.io/index.html). For this I used [gpt4all-falcon-newbpe-q4_0.gguf](https://gpt4all.io/models/gguf/gpt4all-falcon-newbpe-q4_0.gguf)

2. Place the `gguf` file inside the `function` folder, next to the lambda_function.py file.

3. Build the image with docker: `docker build -t nwp:test1 .`.

4. Once built then you can run it locally: `docker run -p 9000:8080 nwp:test1`

5. Once running then you can run invocations against it in another terminal window, such as:
    ```bash
    $response = Invoke-WebRequest -Uri "http://localhost:9000/2015-03-31/functions/function/invocations" -Method POST -Body '{"body": "{\"action\":\"The pirates of the \"}"}' -ContentType 'application/json'
    ```
    ```bash
    $responseContent = $response.Content
    ```
    ```bash
    Write-Output $responseContent
    ```

## AWS deployment
### ECR
Repository Creation in Amazon ECR
- Command: `aws ecr create-repository --repository-name my-lambda-repo-demo`
- Description: Creates a new repository in Amazon Elastic Container Registry (ECR) with the specified name.

Building a Docker Image
- Command: `docker build -t my-lambda-image .`
- Description: Builds a Docker image using the Dockerfile in the current directory and tags it with the specified name.

Authenticating Docker with Amazon ECR
- Command: `aws ecr get-login-password --region (region) | docker login --username AWS --password-stdin (account id).dkr.ecr.(region).amazonaws.com`
- Description: Retrieves an authentication token from ECR and then uses it to log in to the Docker client.

Fetching AWS Account ID
- Command: `aws sts get-caller-identity --query Account --output text`
- Description: Retrieves the AWS account ID for the authenticated user or role.

Tagging the Docker Image for ECR
- Command: `docker tag my-lambda-image:latest (account id).dkr.ecr.(region).amazonaws.com/my-lambda-repo-demo:latest`
- Description: Tags the previously built Docker image with the ECR repository URL.

Pushing the Docker Image to ECR
-Command: `docker push (account id).dkr.ecr.(region).amazonaws.com/my-lambda-repo-demo:latest`
- Description: Pushes the tagged Docker image to the specified ECR repository.

### AWS Lambda
1. CREATE an AWS Lambda function from ECR image.

2. For simplicity, give the Lambda function a [Function URL](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html) and you then you can send HTTP invocations.

4. You can then try it with the URL such as:
    ```bash
    $response = Invoke-WebRequest -Uri "https://INSERTHERE.lambda-url.us-east-1.on.aws/" -Method POST -Body '{"body": "{\"action\":\"The pirates of the \"}"}' -ContentType 'application/json'
    ```
    ```bash
    $responseContent = $response.Content
    ```
    ```bash
    Write-Output $responseContent
    ```

