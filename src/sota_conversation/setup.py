"import packages"
import os
from glob import glob
from setuptools import setup

PACKAGE_NAME = "sota_conversation"
SUBMODULES = "sota_conversation/robot_modules"

setup(
    name=PACKAGE_NAME,
    version="0.0.0",
    packages=[PACKAGE_NAME, SUBMODULES],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + PACKAGE_NAME]),
        ("share/" + PACKAGE_NAME, ["package.xml"]),
        (
            os.path.join("share", PACKAGE_NAME, "launch"),
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
            "talker = sota_conversation.sota_speechpub:main",
            "listener = sota_conversation.sota_speechsub:main",
        ],
    },
)
