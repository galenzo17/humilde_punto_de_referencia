# test_login.py
from browser_use import Browser

def test_login():
    try:
        browser = Browser()
        browser.open('https://tu-dashboard.com/login')
        browser.type('input[name="username"]', 'tu_usuario')
        browser.type('input[name="password"]', 'tu_contraseña')
        browser.click('button[type="submit"]')
        # Verifica que el inicio de sesión fue exitoso
        assert browser.exists('elemento_que_indica_sesion_iniciada')
    except Exception as e:
        print(f"Error durante la prueba de inicio de sesión: {e}")
    finally:
        browser.close()