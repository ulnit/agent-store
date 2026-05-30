from setuptools import setup

setup(
    name='ai-agent-toolkit',
    version='1.0.0',
    description='Essential CLI tools for AI agent developers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='ulnit',
    url='https://github.com/ulnit/ai-agent-toolkit',
    py_modules=['agent_tools'],
    entry_points={
        'console_scripts': [
            'agent-tools=agent_tools:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.8',
)
