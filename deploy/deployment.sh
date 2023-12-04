# docker details
export IMAGE_NAME=community-forum-backend
export IMAGE_VERSION=1.1.1
export FULL_IMAGE_NAME=atishayj2202/${IMAGE_NAME}:${IMAGE_VERSION}

function build() {
  echo "building image ${FULL_IMAGE_NAME}"
  docker build -t "${FULL_IMAGE_NAME}" -f deploy/Dockerfile .
}

function build_and_push_m1() {
  echo "building image ${FULL_IMAGE_NAME} on M1"
#  docker buildx create --use
#  docker buildx build --platform linux/amd64,linux/arm64 -t "${FULL_IMAGE_NAME}" -f deploy/Dockerfile . --push
  docker build --platform linux/amd64 -t "${FULL_IMAGE_NAME}" -f deploy/Dockerfile . --push
}

if [[ $1 = "build" ]]
then
  build
elif [[ $1 = "build-push" ]]
then
  build_and_push_m1
elif [[ $1 = "push" ]]
then
    echo "pushing image ${FULL_IMAGE_NAME}"
    docker push "${FULL_IMAGE_NAME}"