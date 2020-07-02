
doc = '''
#%RAML 1.0
title: Logs API
version: v1
baseUri: https://api.logs.com/{version}
mediaType: application/json


securitySchemes:
  JWT:
    description: We support JWT for authenticating all API requests.
    type: JWT
    describedBy:
      headers:
        Authorization:
          description: |
             Used to send a valid JWT access token. Do not use
             with the "access_token" query string parameter.
          type: string
      queryParameters:
        access_token:
          description: |
             Used to send a valid JWT access token. Do not use with
             the "Authorization" header.
          type: string
      responses:
        401:
          description: |
              Bad or expired token. This can happen if the user or LogsAPI
              revoked or expired an access token. To fix, re-authenticate
              the user.
        403:
          description: |
              Bad JWT request (wrong consumer key, bad nonce, expired
              timestamp...). Unfortunately, re-authenticating the user won't help here.
    settings:
        authorizationUri: https://api.logs.com/{version}/auth/token

traits:
  dataValidation:
    responses:
      400:
        description: A BadRequest happens when data validation fails.
        body:
          properties:
            error: string

types:
    Auth:
        type: object
        discriminator: token
        properties:
            token : string
    Agent:
        type: object
        discriminator: agent_id
        properties:
            agent_id: number
            name: string
            status: boolean
            environment: string
            version: string
            address: string
            user_id: User
        example:
            agent_id: 2
            name: 'teste'
            status: True
            environment: 'Linux'
            version: 1.0
            address: '127.0.0.1'
            user_id: 1
    Event:
        type: object
        discriminator: event_id
        properties: 
            event_id: number
            level: string
            payload: string
            shelved: boolean
            data: date-only
            agent_id: Agent
        example:
            event_id: 2
            level: 'admin'
            payload: {'body': 'teste'}
            shelve: True
            data: '2020-11-02'
            agent_id: 1
    Group:
        type: object
        discriminator: group_id
        properties:
            group_id: number
            name: string
        example:
            group_id: 1
            name: user
    User:
        type: object
        discriminator: user_id
        properties:
            user_id: number
            name: string
            password: string
            email: string
            last_login: datetime
            group_id: Group
        example:
            user_id: 2
            name: 'leo'
            password: 'testesenha'
            email: 'teste@email.com'
            last_login: '2020-09-25T08:30:00-10:45'
            group_id: 1

/auth/token:
    post:
        description: Authenticate user
        is: [dataValidation]
        securedBy: [JWT]
        body:
            type: Auth
            application/json:
                username: admin
                example: |
                    {'username': 'leo',
                     'email':    'teste@email.com',
                     'password': 'testepassword'
                    }
        responses:
            200:
                description: User token succesfully authenticated
            201:
                description: Return the new agent
                body: Auth
            400:
                description: Malformed request syntax
                body:
                    properties:
                        error: string
/agents:
    get:
        description: Get a list of agents
        is: [dataValidation]
        securedBy: [JWT]
        responses:
            200:
                description: Return all agents.
                body: Agent[]
    post:
        description: Add a new agent
        is: [dataValidation]
        securedBy: [JWT]
        body: 
            type: Agent
            application/json:
                        example: |
                            {'name': 'agent',
                             'status': False,
                             'environment': 'Linux',
                             'version': 1.0,
                             'address': 192.168.0.1,
                             'user_id': 2
                            }
        responses:
            201:
                description: Return the new agent
                body: Agent
            401:
                description: Invalid authentication token.
                body:
                    properties:
                        error: string
            409:
                description: The agent already exists in the database
                body:
                    properties:
                        error: string 
    /{id}:
        uriParameters:
            id:
                description: The agent identifier
                type: number
        get:
            description: Gets a specific agent
            is: [dataValidation]
            securedBy: [JWT]
            responses:
                200:
                    description: Returns the specific agent
                    body: Agent
                401:
                    description: Invalid authentication token.
                    body:
                        properties:
                            error: string 
                404:
                    description: Agent not found.
                    body:
                        properties:
                            error: string 
        put:
            description: Updates an already created agent
            is: [dataValidation]
            securedBy: [JWT]
            type: Agent
            body:
                application/json:
                    example: |
                        {'id': 3}
                200:
                    description: Okay.
                401:
                    description: Invalid authentication token.
                404:
                    description: Event not found.
            responses:
                200:
                    description: Returns the updated Event.
                    body: Agent
                401:
                    description: Invalid authentication token.
                    body:
                        properties:
                            error: string
                404:
                    description: Event not found.
                    body:
                        properties:
                            error: string
        delete:
            description: Deletes the agent.
            is: [dataValidation]
            securedBy: [JWT]
            body:
                application/json:
                    example: |
                        {'id': 3}
                200:
                    description: Okay.
                401:
                    description: Invalid authentication token.
                  
            type: Group
            responses:
                200:
                    description: Okay.
                204:
                    description: Confirms the deletion.
                401:
                    description: Invalid authentication token.
                    body:
                        properties:
                            error: string
                404:
                    description: Event not found.
                    body:
                        properties:
                            error: string
    /{id}/events:
        get:
            description: Gets events from a specific event
            is: [dataValidation]
            securedBy: [JWT]
            responses:
                200:
                    description: Returns the event
                    body: Event[]
                401:
                    description: Invalid authentication token.
                    body:
                        properties:
                            error: string
                404:
                    description: Event not found.
                    body:
                        properties:
                            error: string
        post:
            description: Add a new event
            is: [dataValidation]
            securedBy: [JWT]
            type: Group
            body:
                application/json:
                    example: |
                        {'level': 'user',
                         'payload': {'body': 'teste'},
                         'shelve': True,
                         'date': '2020-11-02',
                         'agent_id': 1"
                        }
                    properties:
                        id: number
                        level: string
                        payload: string
                        shelve: boolean
                        date: date
                        agent_id: Agent
                    
                200:
                    description: Okay.
                201:
                    description: Return the new group
                    body: Group
                401:
                    description: Invalid authentication token.
                404:
                    description: Event not found.
            responses:
                201:
                    description: Return the new group
                    body: Group
                401:
                    description: User not authorized. Token required
                    body:
                        properties:
                            error: string        
                409:
                    description: The group already exists in the database
                    body:
                        properties:
                            error: string
        put:
            description: Updates an already created event
            is: [dataValidation]
            securedBy: [JWT]
            type: Event
            body:
                application/json:
                    example: |
                        {'id': 3}
                200:
                    description: Okay.
                401:
                    description: Invalid authentication token.
                404:
                    description: Event not found.
            responses:
                200:
                    description: Returns the updated Event.
                    body: Event
                401:
                    description: Invalid authentication token
                    body:
                        properties:
                            error: string
        delete:
            description: Deletes the user.
            is: [dataValidation]
            securedBy: [JWT]
            type: Group
            body:
                application/json:
                    example: |
                        {'id': 3}
                200:
                    description: Okay.
                401:
                    description: Invalid authentication token.
            responses:
                200:
                    description: Okay.
                204:
                    description: Confirms the deletion.
                401:
                    description: Invalid authentication token.
                    body:
                        properties:
                            error: string
                404:
                    description: Event not found.
                    body:
                        properties:
                            error: string
        /{id}:
            uriParameters:
                id:
                    description: The Event identifier
                    type: number
            get:
                description: Get a specific event from a specific agent
                responses: 
                    200:
                        description: Return the specific event
                        body: Event
/groups:
    get:
        description: Get a list of groups
        is: [dataValidation]
        securedBy: [JWT]
        responses:
            200:
                body: Group[]
            401:
                description: User not authorized. Token required
                body:
                    properties:
                        error: string
    post:
        description: Add a new group
        is: [dataValidation]
        securedBy: [JWT]
        body:
            application/json:
                example: |
                    {'name': 'user'}
                properties:
                    id = number
                    name = string
            type: Group
        responses:
            201:
                description: Return the new group
                body: Group
            401:
                description: User not authorized. Token required
                body:
                    properties:
                        error: string
            409:
                description: The group already exists in the database
                body:
                    properties:
                        error: string       
    /{id}:
        uriParameters:
            id:
                description: The group identifier
                type: number
        get:
            description: Gets a specific group
            is: [dataValidation]
            securedBy: [JWT]
            responses:
                200:
                    description: Returns the specific group
                    body: Group
                404:
                    description: Group not found
                    body:
                        properties:
                            error: string
                401:
                    description: Invalid authentication token
                    body:
                        properties:
                            error: string
        put:
            description: Updates an already created group
            is: [dataValidation]
            securedBy: [JWT]
            body:
                type: Group
            responses:
                200:
                    description: Returns the updated group.
                    body: Group
                401:
                    description: Invalid authentication token
                    body:
                        properties:
                            error: string

        delete:
            description: Deletes the group.
            is: [dataValidation]
            securedBy: [JWT]
            responses:
                204:
                    description: Confirms the deletion.
                401:
                    description: Invalid authentication token
                    body:
                        properties:
                            error: string
/users:
    get:
        description: Get a list of users
        is: [dataValidation]
        securedBy: [JWT]
        responses:
            200:
                description: Returns all the users
                body: User[]
    post:
        description: Add a new user
        is: [dataValidation]
        securedBy: [JWT]
        body:
            type: User
            application/json:
                example: |
                    {'name': 'Leo',
                     'password': 'teste123',
                     'email': 'teste@email.com'
                    }
                properties:
                    id: number
                    name: string
                    password: string
                    email: string
                    last_login: datetime
        responses:
            201:
                description: Returns the new user
                body: User
            401:
                description: Invalid authentication token
                body:
                    properties:
                        error: string
            409:
                description: The user already exists in the database
                body:
                    properties:
                        error: string
    /{id}:
        uriParameters:
            id:
                description: The user identifier
                type: number
        get:
            description: Gets a specific user
            is: [dataValidation]
            securedBy: [JWT]
            responses:
                200:
                    description: Returns the specific user
                    body: User
                401:
                    description: Invalid authentication token
                404:
                    description: User not found
        put:
            description: Updates an already created user
            is: [dataValidation]
            securedBy: [JWT]
            body:
                type: User
            responses:
                200:
                    description: Returns the updated user.
                    body: user
                401:
                    description: Invalid authentication token
                404:
                    description: User not found

        delete:
            description: Deletes the user.
            is: [dataValidation]
            securedBy: [JWT]
            responses:
                200:
                    description: Ok
                204:
                    description: Confirms the deletion.
                401:
                    description: Invalid authentication token
                    body:
                        properties:
                            error: string
                404:
                    description: User not found
                    body:
                        properties:
                            error: string
'''
