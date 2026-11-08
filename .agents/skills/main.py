from foundry_local_sdk import Configuration, FoundryLocalManager

# 1. Créer la configuration
config = Configuration(app_name="monapp")

# 2. Initialiser le Manager
FoundryLocalManager.initialize(config)
manager = FoundryLocalManager.instance

# 3. Accéder au catalogue de modèles
catalog = manager.catalog

# 4. Obtenir le modèle (au lieu de get_model_info)
model = catalog.get_model_variant("qwen2.5-0.5b-instruct-generic-cpu:4")
if not model.is_cached:
    model.download()
model.load()

# Créer une session de chat et envoyer un message
client = model.get_chat_client()
response = client.complete_chat([
    {"role": "user", "content": "Bonjour, qui es-tu ?"}
])
print(response.choices[0].message.content)
