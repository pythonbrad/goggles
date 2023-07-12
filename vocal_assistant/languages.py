ui_languages = {
    "en": {
        "title": 'Voice assistant',
        "analyzing": 'Analyzing',
        "speaking": "Speaking",
        "is_secondary_language": False,
    },
    "fr": {
        "title": 'Assistant vocal',
        "analyzing": "Entrain d'analyser",
        "speaking": "Entrain de parler",
        "is_secondary_language": True,
    }
}

voice_languages = {
    "en": {
        "dont_hear": [
            "Could you please repeat that ? I didn't hear you.",
            "Could you please say that again ? I didn't catch it.",
            "Can you repeat what you said ? I'm having trouble hearing you.",
            "Can you repeat what you just said ? I missed it.",
        ],
        "dont_understand": [
            "Can you repeat yourself ? I can't hear well.",
            "Can you say that again ? I can't understand you.",
            "Can you repeat that ? I couldn't hear clearly.",
            "Could you rephrase that ? I didn't understand.",
            "Can you repeat that statement ? I didn't hear it clearly.",
            "Can you repeat what you mentioned ? I missed some details.",
        ],
        "welcome": [
            "Hello, how can I assist you today ?",
            "Welcome! How can I make your day a little easier ?",
            "Greetings! How may I help you accomplish your tasks ?",
            "Hi there! What can I do to lend a helping hand ?",
            "Welcome! How may I enhance your productivity today ?",
            "Hello, I'm here to assist you with anything you need!",
            "Greetings! How can I simplify your daily routine ?",
            "Hi! How can I assist you in tackling your to-do list ?",
            "Welcome! What can I do to make your life more efficient ?",
            "Hello there! How may I be of service to you today ?",
        ],
        "summarize":
            "Dear customer, I am glad to inform you that there are standing"
            " trips available for booking through our website."
            " You can find all the details using the "
            "following web link. However, please be informed"
            " that the online sales for this trip will end soon. "
            "One departure is scheduled tomorrow for {departures}."
            "The trip is organized by {name_agency} with a average of"
            " {seat_available_count} seats currently available."
            " Don't miss this opportunity to secure your seat before"
            " the online sales end!",
        "no_departure": "Sorry, but no departure is available tomorrow."
    },
    "fr": {
        "dont_hear": [
            "Désolé, pourriez-vous répéter s'il vous plaît ?",
            "Excusez-moi, j'ai des difficultés à comprendre,"
            " pourriez-vous répéter ?",
            "Je n'ai pas tout à fait saisi, pouvez-vous réexprimer"
            " s'il vous plaît ?",
        ],
        "dont_understand": [
            "Pardon, mais je ne vous ai pas bien compris,"
            " pouvez-vous répéter ?",
            "Je n'ai pas bien compris, pourriez-vous reformuler ?",
            "Je n'ai pas saisi clairement, pourriez-vous répéter ?",
            "Excusez-moi, je n'ai pas tout compris, pouvez-vous répéter ?",
            "Je suis désolé(e), je n'ai pas bien compris,"
            " pouvez-vous répéter ?",
            "Veuillez répéter, je n'ai pas tout saisi.",
            "Pardon, je ne suis pas sûr(e) d'avoir bien compris,"
            " pouvez-vous répéter ?",
        ],
        "welcome": [
            "Bienvenue à notre assistance vocale !"
            " Comment puis-je vous aider ?",
            "Bonjour et bienvenue dans notre assistance vocale."
            " Comment puis-je vous aider ?",
            "Bienvenue à bord de notre assistance vocale."
            " Comment améliorer votre expérience aujourd'hui ?",
            "Salut ! Comment puis-je vous aider avec ma voix ?",
            "Bienvenue dans notre assistance vocale."
            " Comment puis-je faciliter votre journée ?",
            "Bonjour ! Comment puis-je vous aider ?",
            "Bienvenue dans notre assistance vocale."
            " Comment puis-je vous offrir une aide précieuse ?",
            "Salut ! Comment puis-je vous aider avec mon assistance ?",
            "Bienvenue dans notre équipe d'assistance vocale."
            " Comment puis-je rendre votre journée plus agréable ?",
            "Bonjour et bienvenue dans notre assistance vocale."
            " Comment puis-je vous simplifier la vie aujourd'hui ?",
        ],
        "summarize":
            "Cher client, je suis heureux de vous informer qu'il y a des departs"
            " de voyage disponibles à la réservation sur notre site Web."
            " Vous pouvez trouver tous les détails en utilisant le lien de siteweb"
            " suivant. Cependant, veuillez être informé que les ventes en ligne"
            " pour ce voyage vont bientôt se terminer."
            " Un départ est prévu pour demain à {departures}."
            " Le voyage est organisé par {name_agency} avec une moyenne de"
            " {seat_available_count} sièges actuellement disponibles."
            " Ne manquez pas cette opportunité de sécuriser votre siège avant"
            " la fin des ventes en ligne!",
        "no_departure": "Je suis désolé, mais il n'a pas de voyage programmer pour demain",
    },
}
