def censurar_insultos(texto):
    # Lista de palabras agresivas (puedes agregar más si lo deseas)
    palabras_agresivas = {"abanto", "abrazafarolas", "adufe", "alcornoque", "alfeñique", "andurriasmo", "arrastracueros", "artabán", "atarre", "baboso", "barrabás", "barriobajero", "bebecharcos", "bellaco", "belloto", "berzotas", "besugo", "bobalicón", "bocabuzón", "bocachancla", "bocallanta", "boquimuelle", "borrico", "botarate", "brasas", "cabestro", "cabezaalberca", "cabezabuque", "cachibache", "cafres", "cagalindes", "cagarruta", "calambuco", "calamidad", "caldúo", "calientahielos", "calzamonas", "cansalmas", "cantamañanas", "capullo", "caracaballo", "caracartón", "caraculo", "caraflema", "carajaula", "carajote", "carapapa", "carapijo", "cazurro", "cebollino", "cenizo", "cenutrio", "ceporro", "cernícalo", "charrán", "chiquilicuatre", "chirimbaina", "chupacables", "chupasangre", "chupóptero", "cierrabares", "cipote", "comebolsas", "comechapas", "comeflores", "comestacas", "cretino", "cuerpoescombro", "culopollo", "descerebrado", "desgarracalzas", "dondiego", "donnadie", "echacantos", "ejarramantas", "energúmeno", "esbaratabailes", "escolimoso", "escornacabras", "estulto", "fanfosquero", "fantoche", "fariseo", "filimincias", "foligoso", "fulastre", "ganapán", "ganapio", "gandúl", "gañán", "gaznápiro", "gilipuertas", "giraesquinas", "gorrino", "gorrumino", "guitarro", "gurriato", "habahelá", "huelegateras", "huevón", "lamecharcos", "lameculos", "lameplatos", "lechuguino", "lerdo", "letrín", "lloramigas", "longanizas", "lumbreras", "maganto", "majadero", "malasangre", "malasombra", "malparido", "mameluco", "mamporrero", "manegueta", "mangarrán", "mangurrián", "mastuerzo", "matacandiles", "meapilas", "melón", "mendrugo", "mentecato", "mequetrefe", "merluzo", "metemuertos", "metijaco", "mindundi", "morlaco", "morroestufa", "muerdesartenes", "orate", "ovejo", "pagafantas", "palurdo", "pamplinas", "panarra", "panoli", "papafrita", "papanatas", "papirote", "paquete", "pardillo", "parguela", "pasmarote", "pasmasuegras", "pataliebre", "patán", "pavitonto", "pazguato", "pecholata", "pedorro", "peinabombillas", "peinaovejas", "pelagallos", "pelagambas", "pelagatos", "pelatigres", "pelazarzas", "pelele", "pelma", "percebe", "perrocostra", "perroflauta", "peterete", "petimetre", "picapleitos", "pichabrava", "pillavispas", "piltrafa", "pinchauvas", "pintamonas", "piojoso", "pitañoso", "pitofloro", "plomo", "pocasluces", "pollopera", "quitahipos", "rastrapajo", "rebañasandías", "revientabaules", "ríeleches", "robaperas", "sabandija", "sacamuelas", "sanguijuela", "sinentraero", "sinsustancia", "sonajas", "sonso", "soplagaitas", "soplaguindas", "sosco", "tagarote", "tarado", "tarugo", "tiralevitas", "tocapelotas", "tocho", "tolai", "tontaco", "tontucio", "tordo", "tragaldabas", "tuercebotas", "tunante", "zamacuco", "zambombo", "zampabollos", "zamugo", "zángano", "zarrapastroso", "zascandil", "zopenco", "zoquete", "zote", "zullenco", "zurcefrenillos"}

    # Divide el texto en palabras
    palabras = texto.split()

    # Reemplaza las palabras agresivas por asteriscos
    palabras = ['*' * len(palabra) if palabra.lower() in palabras_agresivas else palabra for palabra in palabras]

    # Une las palabras de nuevo en una cadena de texto
    texto_censurado = ' '.join(palabras)

    return texto_censurado

# Prueba de la función
texto = "Este es un Abanto y otro Adufe"
print(censurar_insultos(texto))
