from prefect.infrastructure.docker import DockerContainer

docker_block = DockerContainer(
    image="parisakalki/prefect:zoom",
    image_pull_policy="ALWAYS",
    auto_remove=True,
    )


docker_block.save("zoom", overwrite=True)    