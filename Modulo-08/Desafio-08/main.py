doc = '''

#%RAML 1.0

title: challenge-api

mediaType:  application/json

baseUri: http://localhost/challengeapi{version}

version: v1

protocols: [HTTP, HTTPS]

securitySchemes:

  JWT:

    description: We support OAuth 2.0 for authenticating all API requests.

    type: OAuth 2.0

    describedBy:

      headers:

        Authorization:

          type: string

      responses:

        401:

          description: |

            Invalid Token

    settings:

      signatures : ['HMAC-SHA256']


types:

  Auth:

    type: object

    discriminator: token

    properties: 

        token: string


  Agent:

    type: object

    discriminator: agent_id

    properties: 

      agent_id: integer

      user_id: integer

      name: 

        type: string

        maxLength: 50

      status: boolean

      environment:

        type: string

        maxLength: 20

      version: 

        type: string

        maxLength: 20

      address: 

        type: string

        maxLength: 39

    example:

        agent_id: 5

        user_id: 6

        name: teste

        status: true

        environment: teste

        version: v1

        address: 12.33.55.66


  User:

    type: object

    discriminator: user_id

    properties:

      user_id: integer

      name:

        type: string

        maxLength: 50

      email:

        type: string

        maxLength: 254

      password:

        type: string

        maxLength: 50

      last_login:

        type: date-only

      group_id: integer



  Group:

    type: object

    discriminator: group_id

    properties: 

      group_id: integer

      name:

        type: string

        maxLength: 20

    example:

      group_id: 3

      name: teste


  Event:

    type: object

    discriminator: event_id

    properties:

      event_id: integer

      agent_id: integer

      level: 

        type: string

        maxLength: 20

      payload: string

      shelved: boolean

      data: datetime-only

    example:

      event_id: 3

      agent_id: 7

      level: ok

      payload: teste

      shelve: true 

      data: 2020-07-01T07:43:10


/auth/token:

  post:

    description: Gravar um token

    body:

      application/json:

        username: string

        password: string



    responses:

      201:

        body:

          application/json:

            type: Auth

      400:

        body:

          application/json: |

              {"error": "Authentication Error"}         



/agents:

  post:

    description: Adiciona um agent

    securedBy: JWT

    body:

      application/json:

        properties:

        example: |

          {"user_id": 0,

          "name": "teste",

          "status": true,

          "environment": "teste",

          "version": "v1",

          "address": "12.33.55.66"

          }

    responses:

      201:

        body:

          application/json:

            example: |

              {"agent_id": 1}

      401:

        body:

          application/json: |

              {"error": "unauthorized"}

  get:

    description: Retorna Agents

    securedBy: JWT

    responses: 

      200:

        body:

          application/json: Agent []

  /{id}:

    get:

      description: Retorna um Agent por ID

      securedBy: JWT

      responses: 

        200:

          body:

            application/json: Agent

        401:

          body:

            application/json: |

              {"error": "Unauthorized"}

        404:

          body:

            application/json: |

              {"error": "Bad Request"}

    put:

      description: Altera um Agent por ID

      securedBy: JWT

      responses: 

        200:

          body:

            application/json: Agent

        401:

          body:

            application/json: |

              {"error": "Unauthorized"}

        404:

          body:

            application/json: |

              {"error": "Bad Request"}

    delete:

      description: Deleta um Agent por ID

      securedBy: JWT

      responses:

        200:

          body:

            application/json: Agent

        401:

          body:

            application/json: |

              {"error": "Unauthorized"}

        404:

          body:

            application/json: |

              {"error": "Bad Request"}

  /{id}/events:

      post:

        description: Grava um Evento dentro do ID AGent

        securedBy: JWT

        body:

          application/json: Event[]

          responses:

          201:

            body:

              application/json: |

                {"message": "Created"}

          401:

            body:

              application/json: |

                {"error": "Unauthorized"}

          404:

            body:

              application/json: |

                {"error": "Bad Request"}

      get:

        description: Consulta um Evento de um Agent

        securedBy: JWT

        responses:

          200:

            body:

              application/json: Event[]

          401:

            body:

              application/json: |

                {"error": "Unauthorized"}

          404:

            body:

              application/json: |

                {"error": "Bad Request"}

      put:

        description: Altera um Evento de um Agent

        securedBy: JWT

        body:

          application/json: Event[]

          200:

            body:

              application/json: |

                {"message": "Ok"}

          401:

            body:

              application/json: |

                {"error": "Unauthorized"}

          404:

            body:

              application/json: |

                {"error": "Bad Request"}

      delete:

        description: Deleta um Evento de um Agent

        securedBy: JWT

        body:

          application/json: Event[]

          200:

            body:

              application/json: |

                {"message": "Ok"}

          401:

            body:

              application/json: |

                {"error": "Unauthorized"}

          404:

            body:

              application/json: |

                {"error": "Bad Request"}    

      /{id}:

        get:

          description: Consulta um Evento por ID

          securedBy: JWT

          body:

            application/json:

          responses: 

            200:

              body:

                application/json: |

                  {"message": "Ok"}

            401:

              body:

                application/json: |

                    {"error": "unauthorized"}

            404:

              body:

                application/json: |

                  {"error": "Bad Request"}

        post:

          description: Grava um Evento por ID

          securedBy: JWT

          body:

            application/json:

          responses: 

            200:

              body:

                application/json: |

                  {"message": "Ok"}

            401:

              body:

                application/json: |

                    {"error": "unauthorized"}

            404:

              body:

                application/json: |

                  {"error": "Bad Request"}

        put:

          description: Altera um Evento por ID

          securedBy: JWT

          body:

            application/json:

          responses: 

            200:

              body:

                application/json: |

                  {"message": "Ok"}

            401:

              body:

                application/json: |

                    {"error": "unauthorized"}

            404:

              body:

                application/json: |

                  {"error": "Bad Request"}

        delete:

          description: Deleta um Evento por ID

          securedBy: JWT

          body:

            application/json:

          responses: 

            200:

              body:

                application/json: |

                  {"message": "Ok"}

            401:

              body:

                application/json: |

                    {"error": "unauthorized"}

            404:

              body:

                application/json: |

                  {"error": "Bad Request"}

/groups:

  get:

    description: Lista todos os Grupos

    securedBy: JWT

    responses: 

      200:

        body: 

          application/json: Group[]

      401:

        body:

            application/json:

              example: |

                {"error": "unauthorized"}

  post: 

    description: Posta um grupo

    securedBy: JWT

    body:

      application/json:

        properties:

          name: 

            type: string

            maxLength: 20

        example: |

          {"name" : "group_name"}

    responses: 

      201: 

        body:

            application/json: |

              {"message": "Ok"}

      401:

        body:

            application/json: |

                {"error": "unauthorized"}

  put:

    description: Altera um grpo

    securedBy: JWT

    responses:

      200:

        body:

            application/json:

  delete:

    description: Deleta um Grupo

    responses:

      200:

        body:

            application/json:

  /{id}:

    get:

      description: Consulta Grupos por ID

      securedBy: JWT

      responses: 

        200:

          body:

            application/json: Group

        401:

          body:

            application/json: |

                {"error": "Unauthorized"}

        404:

          body:

            application/json: |

              {"error": "Bad Request"}

    put:

      description: Altera um grupo por ID

      securedBy: JWT

      responses:

        200:

          body:

            application/json: |

              {"message": "Ok"}

        401:

          body:

            application/json:

              example: |

                {"error": "unauthorized"}

    delete:

      description: Deleta um grupo por ID

      securedBy: JWT

      responses:

        200:

          body:

            application/json: |

              {"message": "Ok"}

        401:  

          body:

            application/json: |

                {"error": "Unauthorized"}

        404:

          body:

            application/json: |

                {"error": "Bad Request"}

/users:

  post:

    description: Grava um novo usuário

    securedBy: JWT

    body:

      application/json:

        properties:

          name:

            type: string

            maxLength: 50

          password:

            type: string

            maxLength: 50

          email:

            type: string

            maxLength: 254

          last_login:

            type: date-only

        example: |

            {"name": "User",

            "email": "olavobilacl@olavobilac.com.br",

            "password": "olavoopoeta",

            "last_login": "2020-01-01"

            }

    responses:

      201:

        body:

            application/json: |

                {"message": "Ok" }



      401:

        body:

            application/json: |

                {"error": "unauthorized"}

  get:

    description: Consulta Usuário

    securedBy: JWT

    responses:

      200:

        body:

            application/json: User[]

      401:

        body:

            application/json: |

              {"error": "unauthorized"}


  /{id}:

    get: 

      description: Consulta usuário por ID

      securedBy: JWT

      responses:

        200:

          body:

            application/json: User

        401:

          body:

            application/json: |

              {"error": "unauthorized"}

        404:

          body:

            application/json: |

              {"error": "Bad Request"}


    put:

      description: Altera usuário por ID

      securedBy: JWT

      responses:

        200:

          body:

            application/json: |

              {"message": "Ok"}

        401:

          body:

            application/json: |

              {"error": "unauthorized"}

        404:

          body:

            application/json: |

              {"error": "Bad Request"}

    delete:

      description: Deleta usuário por ID

      securedBy: JWT

      responses:

        200:

          body:

            application/json: |

              {"message": "Ok"}

        401:

          body:

            application/json: |

              {"error": "unauthorized"}

        404:

          body:

            application/json: |

              {"error": "Bad Request"}

'''