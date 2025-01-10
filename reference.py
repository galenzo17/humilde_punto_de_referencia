from browser_use import Browser

def test_login():
    try:
        # Inicializa el navegador en modo headless
        browser = Browser(headless=True)

        # Abre la página de inicio de sesión
        browser.open('http://localhost:8080')

        # Ingresa las credenciales
        browser.type('input[name="username"]', 'user')
        browser.type('input[name="password"]', 'pass')

        # Envía el formulario de inicio de sesión
        browser.click('button[type="submit"]')

        # Espera a que la página de usuarios se cargue
        browser.wait_for_element('a[href="/users"]')

        # Navega a la sección de usuarios
        browser.click('a[href="/users"]')

        # Verifica que la lista de usuarios esté presente
        assert browser.exists('table#user_list')

        print("Prueba de inicio de sesión y navegación exitosa.")
    except Exception as e:
        print(f"Error durante la prueba: {e}")
    finally:
        # Cierra el navegador
        browser.close()

if __name__ == "__main__":
    test_login()