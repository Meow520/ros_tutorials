import os
from glob import glob
from setuptools import find_packages, setup

package_name = "sota_hello"
submodules = "sota_hello/robot_modules"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name, submodules],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (
            os.path.join("share", package_name, "launch"),
            glob(os.path.join("launch", "*launch.[pxy][yma]*")),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="mao",
    maintainer_email="mao.montlevre@gmail.com",
    description="Sota Operation Tutorial",
    license="Apache Lisence 2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "talker = sota_hello.sota_speechpub:main",
            "listener = sota_hello.sota_speechsub:main",
            "service = sota_hello.sota_service:main",
            "client = sota_hello.sota_client:main",
        ],
    },
)
