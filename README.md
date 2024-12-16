# humilde_punto_de_referencia
Este proyecto trata de verificar y medir resultados de llms en español

Narración con restricciones cambiantes:
Instrucción inicial: "Crea una historia corta de fantasía sobre un joven aprendiz de mago que debe recuperar un talismán robado."
Restricción progresiva: A mitad de la historia, exige que el aprendiz pierda temporalmente la memoria, y que deba interactuar con un personaje cómico que habla en rimas. Al final, pide que el desenlace sea contado desde la perspectiva de un cuervo parlante.
Criterio a evaluar: Coherencia narrativa, adaptación a los cambios y mantenimiento del hilo conductor.

Enigma lógico bajo presión:
Instrucción inicial: "Tienes tres cofres: uno contiene oro, otro contiene plata y el último está vacío. Las etiquetas que indican su contenido están todas mal colocadas. Identifica el contenido de cada cofre con la mínima cantidad de preguntas."
Cambio repentino: Una vez dada la respuesta inicial, exigir una nueva solución: "Si ahora uno de los cofres se vuelve transparente y ves que contiene algo desconocido (un mineral raro), ¿cómo actualizarías la estrategia?"
Criterio a evaluar: Capacidad de razonar lógicamente, reformular ante nueva información y mantener coherencia.

Plan de negocios sostenible:
Instrucción inicial: "Diseña un plan de negocios para una cafetería móvil de café orgánico, dirigida a universitarios con bajo presupuesto y en zonas con poca infraestructura."
Contratiempo adicional: A mitad de la propuesta, introducir que el precio del café orgánico se duplica y que la competencia comienza a ofrecer café con descuento.
Criterio a evaluar: Innovación del plan, ajuste estratégico ante dificultades, realismo financiero.

Poema con restricciones lingüísticas:
Instrucción inicial: "Crea un poema corto en verso libre sobre el mar."
Restricción adicional: En la segunda versión, incluir las palabras 'escafandra', 'eléctrico' y 'suspiro', y mantener un ritmo cercano al pentámetro yámbico.
Criterio a evaluar: Creatividad poética, adaptación a restricciones y calidad estética.

Problema matemático reinterpretado:
Instrucción inicial: "Resuelve: 2x + 3 = 9. Explica el proceso matemático."
Transformación posterior: Ahora, explica la misma solución pero como si fuera un cuento para niños, donde 'x' es un perrito que busca huesos (cada paso matemático se vuelve un evento narrativo).
Criterio a evaluar: Exactitud matemática, capacidad de reinterpretación sin perder el contenido esencial.

Simulación de crisis empresarial:
Instrucción inicial: "Una librería independiente está sufriendo pérdidas por la competencia en línea. Diseña una estrategia de marketing para atraer clientes al local físico."
Evento imprevisto: A mitad de la estrategia, informar que la ciudad impone una nueva tasa impositiva al papel impreso y que un gran inversor se retira. Ajustar la estrategia.
Criterio a evaluar: Capacidad de resiliencia ante problemas, coherencia y viabilidad del plan actualizado.

Lenguaje inventado:
Instrucción inicial: "Inventa un lenguaje con cinco palabras para nombrar objetos, dos reglas gramaticales simples para formar frases, y demuéstralo con tres oraciones."
Desafío posterior: Añade una nueva palabra y explica cómo cambia la estructura de una oración compleja con ella.
Criterio a evaluar: Creatividad, coherencia interna, aplicación consistente de las reglas.

Experimento científico inusual:
Instrucción inicial: "Diseña un experimento para comprobar si los conejos prefieren zanahorias frescas o congeladas en días de lluvia. Explica variables independientes, dependientes y de control."
Cambio de condiciones: Ahora, indica qué harías si llueve menos de lo esperado o si los conejos presentan estrés. ¿Cómo ajustas el experimento?
Criterio a evaluar: Rigor científico, flexibilidad ante cambios y claridad metodológica.

Mediación de conflicto social:
Instrucción inicial: "Hay un conflicto entre granjeros que quieren más terreno para cultivos y conservacionistas que desean preservar un bosque. Propón una estrategia de mediación."
Nuevo elemento: Introduce a un tercero: un grupo de turismo ecológico que quiere rutas de senderismo seguras. Ajusta la propuesta para satisfacer a los tres grupos.
Criterio a evaluar: Equilibrio, negociación creativa, coherencia en la propuesta.

Múltiples soluciones a un reto creativo:
Instrucción inicial: "Diseña tres logotipos distintos para una marca de helados: uno minimalista, otro retro y otro futurista."
Refinamiento posterior: Tras crear los tres, pide mejorar el logotipo retro agregando un elemento que indique sostenibilidad sin perder el estilo.
Criterio a evaluar: Diversidad creativa inicial, capacidad de perfeccionar un concepto existente y mantener la coherencia visual.

Agente que controla una computadora: Automatización de tareas
Instrucción inicial: "Imagina que tienes acceso a una terminal Linux. Necesito que crees un script en Bash que busque todos los archivos .txt en el directorio /home/user/docs modificados en la última semana, los comprima en un archivo backup.tar.gz y los mueva a /home/user/backups."
Evaluación: Se observa si el modelo produce comandos lógicos, la sintaxis correcta del script y comprende la estructura del sistema de archivos y herramientas estándar (como find, tar, mv).

Agente que controla una computadora: Gestión de paquetes
Instrucción inicial: "Estás en un entorno Ubuntu. Necesito que actualices el sistema, instales el servidor web Nginx, lo configures para servir un sitio estático desde /var/www/html y habilites el firewall para permitir tráfico HTTP."
Evaluación: Se analiza si el modelo describe adecuadamente los comandos apt, la edición de archivos de configuración de Nginx, el uso de ufw y la comprensión del flujo para poner un servicio en marcha.

Agente de investigación: Síntesis de información compleja
Instrucción inicial: "Necesito un resumen crítico de las últimas técnicas en aprendizaje por refuerzo profundo (Deep Reinforcement Learning), incluyendo referencias a dos papers importantes publicados en los últimos 3 años. Explica las diferencias entre ellos, sus ventajas, limitaciones y casos de aplicación."
Evaluación: Se mide la capacidad para extraer y sintetizar información, citar papers relevantes (reales o hipotéticos, según se defina el criterio), y presentar un análisis coherente, estructurado y neutral.

Agente de investigación: Verificación de hechos
Instrucción inicial: "He leído que la dieta cetogénica previene el Alzheimer al 100%. ¿Es esto cierto? Proporciona evidencia científica, menciona estudios concretos (si existieren) y da un veredicto sobre la veracidad de esta afirmación."
Evaluación: Se examina la habilidad del modelo para confrontar la desinformación, verificar hechos, citar fuentes fiables y presentar un argumento equilibrado.

Agente de investigación: Comparativa de herramientas
Instrucción inicial: "Necesito elegir entre usar Docker o Podman para la virtualización de contenedores en un entorno de producción. Resume las principales diferencias, ventajas y desventajas, y emite una recomendación basada en seguridad, facilidad de uso y soporte."
Evaluación: Se observa la capacidad de contrastar herramientas, exponer pros y contras y ofrecer una recomendación informada.

Agente de atención al cliente: Manejo de una queja compleja
Instrucción inicial: "Un cliente escribe muy molesto porque su pedido de flores para un aniversario llegó marchito y un día tarde. Responde con empatía, ofrece una compensación razonable y evita términos defensivos, intentando mantener la relación con el cliente."
Evaluación: Se valora la empatía, el tono cortés, la claridad en ofrecer una solución (reembolso, descuento, remplazo gratuito) y la habilidad para calmar la situación.

Agente de atención al cliente: Explicación de un proceso complicado
Instrucción inicial: "Un usuario pregunta cómo tramitar una devolución internacional de un producto adquirido en tu tienda online. Explica paso a paso el proceso, incluyendo el llenado de formularios, costos potenciales, tiempos de espera y opciones de contacto."
Evaluación: Claridad de la explicación, organización de la información, tono amable y orientación al usuario.

Agente de atención al cliente: Adaptación de políticas
Instrucción inicial: "Un cliente solicita un reembolso completo de un producto que ya ha utilizado durante 30 días, aunque nuestra política sólo lo permite hasta 15 días. El cliente argumenta razones personales. Propón una respuesta que intente mantener la satisfacción del cliente sin infringir las normas de la empresa."
Evaluación: Habilidad para aplicar políticas de forma flexible, ofreciendo soluciones alternativas (un crédito en tienda, un descuento futuro) y manteniendo un tono comprensivo.

Agente que controla una computadora: Depuración de un problema
Instrucción inicial: "En un servidor remoto, la aplicación web en Python ha dejado de responder. Proporciona pasos para diagnosticar el problema: revisar logs en /var/log, verificar el estado del servicio con systemctl, chequear el uso de recursos con top y df -h, y proponer soluciones si el proceso se encuentra caído."
Evaluación: Se observa la lógica y exhaustividad en la resolución de problemas, el orden de los pasos y la claridad al comunicarlo.

Agente de investigación y análisis estratégico:
Instrucción inicial: "La empresa X quiere expandirse a un nuevo mercado internacional. Necesito un análisis FODA (Fortalezas, Oportunidades, Debilidades, Amenazas) tomando en cuenta tendencias globales actuales, barreras de entrada y competidores locales. Ofrece además recomendaciones estratégicas."
Evaluación: Se examina la profundidad del análisis, el uso coherente del marco FODA, la identificación de factores externos e internos y la capacidad de ofrecer consejos accionables.
