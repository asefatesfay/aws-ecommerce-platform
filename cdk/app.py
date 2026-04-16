#!/usr/bin/env python3

import aws_cdk as cdk

from stacks.application_stack import ApplicationStack
from stacks.config import load_settings
from stacks.data_stack import DataStack
from stacks.frontend_stack import FrontendStack
from stacks.identity_stack import IdentityStack
from stacks.messaging_stack import MessagingStack
from stacks.network_stack import NetworkStack


app = cdk.App()
settings = load_settings(app)

environment = cdk.Environment(
    account=settings.account,
    region=settings.region,
)

network_stack = NetworkStack(
    app,
    f"{settings.stack_prefix}Network",
    settings=settings,
    env=environment,
)

data_stack = DataStack(
    app,
    f"{settings.stack_prefix}Data",
    settings=settings,
    env=environment,
)

identity_stack = IdentityStack(
    app,
    f"{settings.stack_prefix}Identity",
    settings=settings,
    env=environment,
)

messaging_stack = MessagingStack(
    app,
    f"{settings.stack_prefix}Messaging",
    settings=settings,
    env=environment,
)

application_stack = ApplicationStack(
    app,
    f"{settings.stack_prefix}Application",
    settings=settings,
    cluster=network_stack.cluster,
    listener=network_stack.http_listener,
    vpc=network_stack.vpc,
    env=environment,
)
application_stack.add_dependency(network_stack)

frontend_stack = FrontendStack(
    app,
    f"{settings.stack_prefix}Frontend",
    settings=settings,
    env=environment,
)

frontend_stack.add_dependency(network_stack)

cdk.Tags.of(app).add("Project", settings.project)
cdk.Tags.of(app).add("Environment", settings.environment)
cdk.Tags.of(app).add("ManagedBy", "cdk")

app.synth()
