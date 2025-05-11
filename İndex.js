const Alexa = require('ask-sdk-core');

const moodResponses = {
    "üzgün": "Bazen üzgün hissetmek doğaldır. Unutma, her fırtınanın sonunda güneş açar.",
    "mutlu": "Harika! Bu enerjiyi paylaşmayı unutma, mutluluk bulaşıcıdır.",
    "aşık": "Aşk ne güzel bir duygu! Tadını çıkar ama kalbini de koru.",
    "yalnız": "Yalnız hissettiğinde bile, unutma ki bu dünyada seni anlayan birileri mutlaka vardır.",
    "nostaljik": "Geçmiş güzel anılarla doludur ama gelecekte seni daha fazlası bekliyor."
};

function getSongMood(songName) {
    if (songName.toLowerCase().includes("ağla") || songName.toLowerCase().includes("hüzün"))
        return "üzgün";
    if (songName.toLowerCase().includes("dans") || songName.toLowerCase().includes("neşe"))
        return "mutlu";
    if (songName.toLowerCase().includes("aşk"))
        return "aşık";
    if (songName.toLowerCase().includes("yalnız") || songName.toLowerCase().includes("tek başıma"))
        return "yalnız";
    if (songName.toLowerCase().includes("eski") || songName.toLowerCase().includes("nostalji"))
        return "nostaljik";

    return "mutlu";
}

const PlaySongIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'PlaySongIntent';
    },
    handle(handlerInput) {
        const songName = handlerInput.requestEnvelope.request.intent.slots.songName.value;
        const mood = getSongMood(songName);
        const responseMessage = moodResponses[mood] || "Şarkının modunu anlayamadım ama keyfini çıkar!";

        const speakOutput = `Şimdi ${songName} çalıyor. ${responseMessage}`;
        return handlerInput.responseBuilder.speak(speakOutput).getResponse();
    }
};

const LaunchRequestHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'LaunchRequest';
    },
    handle(handlerInput) {
        return handlerInput.responseBuilder
            .speak('Hoş geldin. Lütfen bir şarkı söyle ve ruh haline göre sana bir söz söyleyeyim.')
            .reprompt('Lütfen bir şarkı ismi söyle.')
            .getResponse();
    }
};

exports.handler = Alexa.SkillBuilders.custom()
    .addRequestHandlers(
        LaunchRequestHandler,
        PlaySongIntentHandler
    )
    .lambda();
