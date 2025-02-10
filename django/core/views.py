def dashboard_callback(request, context):
    print("ciao")
    context.update({
        "custom_variable": "value",
    })

    return context