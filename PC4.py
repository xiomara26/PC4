# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta 
# o abrimos el folder desde visual Studio Code 


# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
#python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# streamlit run PC4.py
# python -m streamlit run PC4.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.

# Creamos la lista de páginas
paginas = ['Inicio', 'Experiencia', 'Gráficos']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Inicio':

    # TITULO DE LA PAGINA INICIO: La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>MI BLOG PERSONAL: ¡aprendí a programar! 👩‍💻</h1>", unsafe_allow_html=True)

    # <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # Pueden agregar emojis en el texto de Markdown utilizando códigos de emoji, por ejemplo:
    # <h1 style='text-align: center;'>Aquí escribe un nombre creativo para tu blog 📝</h1>
    # También pueden personalizar el color del texto utilizando el atributo style, por ejemplo:
    # <h1 style='text-align: center; color: blue;'>Nombre de tu blog</h1>
    # El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # COLUMNAS: En la primera columna colocamos la imagen de perfil
    col1.image("Foto.jpg", caption='Esta soy yo c: ', width=300)

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

    texto = """
    ¡Hola! Me llamo Xiomara, pero me gusta que me digan Xio 😊. Nací en Huancayo, que se ubica en la región Junín. Sin embargo, ahora vivo en Lima junto a mi hermana quien también estudia en la misma universidad que yo. Cada fin de semestre me emociona volver a mi ciudad y pasar más tiempo con toda mi familia. 
    Estudio la carrera de comunicación audiovisual en la PUCP 🎓 y lo que me gusta de esta carrera es la versatilidad de la misma para desenvolverse en múltiples campos. La creación de contenidos audiovisuales es un elemento esencial en la sociedad en la que vivimos hoy en día. Nos conocemos, nos informamos, interactuamos a través de contenidos audiovisuales, por eso es importante entender que estamos creando y consumiendo. Cada video, aunque parezca irrelevante, siempre está cargado de significado. Y cuando se trata de contenido de gran relevancia social, es importante que quienes los produzcan asuman esa responsabilidad con conciencia.  
    También me gusta mucho el cine 🍿. Gracias a mi carrera, he podido conocer más sobre el lenguaje cinematográfico. Productos que antes ya disfrutaba, ahora me resultan más interesantes al entender porque causaban diversos sentimientos y emociones más allá de lo que decía en palabras.
    En el futuro, me gustaría ejercer mi carrera al servicio de una causa social. Me interesa la idea de trabajar con una ONG o alguna organización enfocada en el acceso a la educación y en mejorar la calidad de vida de niñas, niños pequeños y mujeres.
    En mi tiempo libre, me encanta escuchar música 🎶 y cantar a la par, aunque no soy una buena cantante, pero es divertido hacerlo. También me gusta bailar, sobre todo canciones de kpop, que tienen bailes muy dinámicos y entretenidos. Además, me gusta jugar Roblox 🎮, una plataforma de videojuegos en línea. Muchas personas dicen que solo es u uego para niños pequeños, pero los juegos dentro son muy entretenidos. A veces me conecto con mis amigos y otras veces juego sola. Esas son las actividades que realizó principalmente cuando estoy en Lima, pero cuando vuelvo a mi ciudad natal, Huancayo, realizo ¿más actividades. Como allá tengo la mayoría de mis cosas y materiales, ahí me gusta tejer, tocar el violín y la guitarra, aunque esta última recién la estoy aprendiendo, y ocasionalmente pinto 🎨.    
    """

    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    
    # Mostramos el texto
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
    # La etiqueta <div> se utiliza para agrupar contenido en HTML. 
    # En este caso, el texto está justificado (text-align: justify;). 
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto} se reemplaza por el valor de la variable texto.

elif  pagina_seleccionada == 'Experiencia':

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻✨</h1>", unsafe_allow_html=True)

    # En esta sección debes describir y comentar tu experiencia aprendiendo a programar
    # ¿Cómo te sentiste al principio?, 
    # ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
    # ¿Qué te gustaría hacer con la programación en el futuro? 

    # Agregar un  texto para la respuesta
    texto_2 = """
    Al inicio, sí tenía un poco de miedo 😟, porque ¡no sabía nada de programación! Lo único que sabía era por las películas, y en ellas se muestra como algo super complejo. Sin embargo, también me causaba mucha intriga saber cómo funcionaba. No tenía idea de que literalmente todo en línea trabajaba de esa manera. En las primeras clases, fui empezando a entender cosas básicas, y la verdad fue divertido, así que iba jugando con los códigos a ver qué me salía.
    Creo que lo mejor que me ha enseñado la programación es que un problema o situación no tiene una sola solución, sino que tiene miles de maneras creativas 💡. Y esto no solo se queda en la programación, sino que aplica para la vida misma. Otra cosa que me enseñó fue a tener paciencia y ser ordenada, porque un solo error en el código puede malograrlo todo 😅.
    Lo que me gusta de programar es que puedo crear cualquier cosa que se me venga a la mente. Al inicio, vimos ejemplos más prácticos con números, pero cuando fuimos viendo juegos para entender los métodos, ¡las clases de PCC se volvieron mis favoritas! Así que, a partir de ese momento, cuando no entendía cómo funcionaba algo, trataba de usar una temática divertida y linda… ¡como en los juegos! Algunas cosas que programé que me gustaron mucho fueron: ¿QUÉ DICE TU ANIMAL FAVORITO DE TÍ?, ¡ADIVINA QUÉ FRUTAS TENGO EN MI CESTA! o ¡ADIVINA EN QUÉ PLANETA ESTOY PENSANDO!
    En el futuro, creo que va a ser clave emplear la programación en mi carrera 🚀. Lo que me gustaría hacer con ella sería justamente automatizar procesos que me tomarían más tiempo, para dedicar el resto a la creación creativa de propuestas. Como mencionaba, me gusta mucho la idea de trabajar con una ONG en el futuro, y en especial en relación a la educación. Creo que usar la programación para crear programas amigables e interactivos que puedan colaborar en la educación de niños y niñas pequeñas sería increíble.
    Al inicio del curso, no pensé que me terminaría gustando tanto, pero creo que el manejo de contenidos y la manera de enseñar de nuestra JP Luisa fue clave para este cambio en mi manera de ver la programación ❤️.
   
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el texto está justificado (text-align: justify;).
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto_2.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto_2} se reemplaza por el valor de la variable texto.

    # Agregamos un subtítulo para el video
    st.markdown("<h2 style='text-align: center;'>Cuando aprendí a usar condicionales 🤓</h2>", unsafe_allow_html=True)
    
    # <h2 style='text-align: center;'>Aquí escribe un nombre creativo para presentar tu video</h2>: Esta es una cadena de código HTML.
    # La etiqueta <h2> se utiliza para un encabezado de segundo nivel en una página web.
    # El texto está centrado (text-align: center;).
    # El texto dentro de las etiquetas <h2> ("Aquí escribe un nombre creativo para presentar tu video") es el contenido del encabezado.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.
    # Por ejemplo, puedes agregar un emoji de video 🎥 

    # Agregamos un video realizado en las practicas anteriores
    st.video("https://youtu.be/rJnLPgrkigM")

    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E"): Esta línea está mostrando un video en la aplicación web.
    # La función video toma como primer argumento la URL del video que se desea mostrar.
    # En este caso, la URL es "https://www.youtube.com/watch?v=X_Z7d04x9-E".
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.

    # O creamos un botón para ir al enlace del video con button (drive)
    st.markdown(f"<div style='text-align: center;'><a href='https://youtu.be/rJnLPgrkigM' target='_blank'><button>Ver video</button></a></div>", unsafe_allow_html=True) 

    # <div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>:
    # Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el contenido está centrado (text-align: center;).
    # La etiqueta <a> se utiliza para crear un enlace.
    # El atributo href especifica la URL a la que se dirige el enlace.
    # En este caso, la URL es 'https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link'.
    # El atributo target='_blank' indica que el enlace se abrirá en una nueva pestaña del navegador.
    # La etiqueta <button> se utiliza para crear un botón.
    # El texto dentro de las etiquetas <button> ("Ver video") es el contenido del botón.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.
    
else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'>Algunos gráficos que diseñé 💪📈</h1>", unsafe_allow_html=True)

    # Creamos una lista de gráficos
    graficos = ['Gráfico doble de barras de los seguidores en TikTok de las entidades públicas de salud 2021-2025', 'Gráfico pastel de los tipos de programas en Netflix', 'Mapa de mis películas favoritas']

    # Creamos un cuadro de selección en la página de gráficos
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # El cuadro de selección se crea con la función selectbox.
    # El primer argumento es el texto que se muestra en el cuadro de selección.
    # El segundo argumento es una lista de opciones que se pueden seleccionar.
    # En este caso, las opciones son los elementos de la lista graficos.
    # La opción seleccionada se asigna a la variable grafico_seleccionado.
    # La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
    

    # Mostramos el gráfico seleccionado (El primer if: primer gráfico)
    if grafico_seleccionado == 'Gráfico doble de barras de los seguidores en TikTok de las entidades públicas de salud 2021-2025':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>En este gráfico, se puede ver el crecimiento del número de seguidores de la cuentas de TikTok de las entidades públicas de salud 🏥 del Perú como el Ministerio de Salud, EsSalud, Direccion de Redes Integradas de Salud Lima Centro, Direccion de Redes Integradas de Salud Lima Este, Direccion de Redes Integradas de Salud Lima Sur, Direccion de Redes Integradas de Salud Lima Norte. En color rosa 🌸, se aprecia en número de seguidores en el año 2021 y de color naranja 🏵️ los del año 2025.</div>", unsafe_allow_html=True)
        st.image("Grafico_doble_barras.png", caption='Gráfico de los seguidores en TikTok de las entidades publicas de salud 2021-2025 🏥', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico pastel de los tipos de programas en Netflix':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>En este grafico de pastel, podemos visualizar de forma porcentual la distribución de los tipos de contenidos disponibles en la plataforma de Netflix. Notablemente, existe una mayor cantidad de programas tipo Movie 🎬 en comparación al TV Show 📺. Este tipo de grafico resulta útil para apreciar rápidamente y de manera general la proporción que cada elemento ocupa.</div>", unsafe_allow_html=True)
        st.image("tipo_programas.png", caption='Gráfico pastel de los tipo de programas en Netflix🎥', width=500)
        pass
    elif grafico_seleccionado == 'Mapa de mis películas favoritas':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>En este mapa, ubiqué los lugares donde se grabaron mi top 5 películas favoritas 🎬. En el caso de las películas con actores reales, como Orgullo y Prejuicio, Los juegos del hambre y Alicia en el país de las maravillas, marqué algunas locaciones reales que fueron utilizadas en la filmación. En Orgullo y Prejuicio: Chatsworth House → Representa la residencia de Mr. Darcy: Pemberley. En Los juegos del hambre: Shelby, Carolina del Norte, EE. UU. → Fue el lugar donde se grabó la ceremonia de selección del Distrito 12. En Alicia en el país de las maravillas: National Trust – Antony → Escenario de la casa donde se celebra la fiesta de compromiso de Alicia, en el mundo real. Por otro lado, en el caso de las películas animadas —La princesa y el sapo y Shrek— señalé los estudios donde fueron producidas: Walt Disney Studios 🏰 y Dreamworks Animation 🌙. Puede que en el mapa no los veas 😅, pero solo acércate un poco, porque son vecinas  (¡y rivales!⚔️). Asimismo, en cada una verás detalles como el año de estreno y director o directora de la película.</div>", unsafe_allow_html=True)
        # Si "mapa_cusco.html" es un archivo HTML (no una imagen), debes mostrarlo con st.components.v1.html
        import streamlit.components.v1 as components
        with open("mapa_peliculas.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass

    # if grafico_seleccionado == 'Gráfico de barras verticales de lenguas aisladas':
    # st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
    # st.image("aisladas_base_datos.png", caption='Gráfico de lenguas aisladas', width=500): Esta línea está mostrando una imagen en la aplicación web.
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar.
    # En este caso, la imagen es "aisladas_base_datos.png".
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen,
    # en este caso "Gráfico de lenguas aisladas".
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 500 píxeles.

    # elif grafico_seleccionado == 'mapa_cusco':
    # import streamlit.components.v1 as components
    # with open("mapa_cusco.html", "r", encoding="utf-8") as f:
    #     html_content = f.read()
    # components.html(html_content, height=500): Esta línea está mostrando un archivo HTML en la aplicación web.
    # La función components.html toma como primer argumento el contenido HTML que se desea mostrar.
    # En este caso, el contenido HTML se lee desde el archivo "mapa_cusco.html".
    # El argumento height se utiliza para especificar la altura del contenido HTML, en este caso 500 píxeles.
    
    # Si no tenemos el archivo HTML, podemos agregar el código para crear el mapa de Cusco directamente en Streamlit.
    # Primero debes crear el diccionario de coordenadas del mapa de Cusco.
    # Luego debes crear el mapa utilizando la librería folium y streamlit-folium.
    # pip install folium
    # pip install streamlit-folium
        #import folium
        #from streamlit_folium import st_folium

        # Mostrar el mapa en Streamlit
        #st_folium(mapa_cusco, width=700, height=500)
    
