from flask import render_template_string


def test_render_field(app, client, hello_form):
    @app.route("/field")
    def test():
        form = hello_form()
        return render_template_string(
            """
            {% from 'rings/wtf.html' import render_field %}
            {{ render_field(form.username) }}
            {{ render_field(form.password) }}
            """,
            form=form,
        )

    response = client.get("/field")
    data = response.get_data(as_text=True)
    print(data)
    assert '<input class="custom-text " id="username" name="username" required' in data
    assert '<input class="custom-text " id="password" name="password" required' in data


def test_render_form(app, client, hello_form):
    @app.route("/form")
    def test():
        form = hello_form()
        return render_template_string(
            """
            {% from 'rings/wtf.html' import render_form %}
            {{ render_form(form) }}
            """,
            form=form,
        )
        
    response = client.get("/form")
    data = response.get_data(as_text=True)
    assert '<input class="custom-text " id="username" name="username"' in data
    assert '<input class="custom-text " id="password" name="password"' in data


def test_render_nav_item(app, client):
    @app.route("/nav_item")
    def test():
        return render_template_string(
            """
            {% from 'rings/nav.html' import render_nav_item %}
            {{ render_nav_item('test', 'Home')}}
            """
        )

    response = client.get("/nav_item")
    data = response.get_data(as_text=True)
    assert '<a class="text-white active"' in data
