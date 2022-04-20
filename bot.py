# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
import requests

date = []
muzica = []
artist = []


async def feeling(f, turn_context: TurnContext):
    await turn_context.send_activity(f"La cum te simti pot sa-ti recmand niste muzica.")
    if f == 'trist':
        date.append('trist')
        muzica.append('pop')
        muzica.append('lo-fi')
        muzica.append('sad music')
        await turn_context.send_activity(f"M-am gandit la niste muzica pop, lo-fi, sad music. Alege un gen.")
    if f == 'fericit':
        date.append('fericit')
        muzica.append('house')
        muzica.append('trap')
        muzica.append('pop')
        await turn_context.send_activity(f"M-am gandit la niste muzica house, trap, pop. Alege un gen.")
    if f == 'ganditor':
        date.append('ganditor')
        muzica.append('lo-fi')
        muzica.append('indie')
        await turn_context.send_activity(f"M-am gandit la niste muzica lo-fi, indie. Alege un gen.")
    if f == 'hyped':
        date.append('hyped')
        muzica.append('house')
        muzica.append('EDM')
        muzica.append('dubstep')
        await turn_context.send_activity(f"M-am gandit la niste muzica house, EDM, dubstep. Alege un gen.")


async def preferinte(datePrimite, turn_context: TurnContext):
    text = turn_context.activity.text

    if text in muzica:
        date.append(text)
        await turn_context.send_activity(f"Vrei un playlist sau artist?")
    elif text == 'playlist':
        # pop, lo-fi, sad music, trap, indie,house, EDM, dubstep
        await turn_context.send_activity(f"Am pregatit un playlist perfect pentru tine.")
        if date[1] == 'pop':
            await turn_context.send_activity(
                f"https://open.spotify.com/playlist/37i9dQZF1DWVlLVXKTOAYa?si=c73b96f8e4684f48")
            await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
            date.clear()
            muzica.clear()
        if date[1] == 'lo-fi':
            await turn_context.send_activity(
                f"https://open.spotify.com/playlist/37i9dQZF1DWWQRwui0ExPn?si=f0062c3dc2004b81")
            await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
            date.clear()
            muzica.clear()
        if date[1] == 'sad music':
            await turn_context.send_activity(
                f"https://open.spotify.com/playlist/44tRfteJJzAmUONSiA56bQ?si=61913eb2339b420e")
            await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
            date.clear()
            muzica.clear()
        if date[1] == 'trap':
            await turn_context.send_activity(
                f"https://open.spotify.com/playlist/4nqsgbmBaSFhN8EwJk7Nu0?si=c6b70f941ca8479a")
            await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
            date.clear()
            muzica.clear()
        if date[1] == 'indie':
            await turn_context.send_activity(
                f"https://open.spotify.com/playlist/37i9dQZF1DWWEcRhUVtL8n?si=fdb90feb34224f8a")
            await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
            date.clear()
            muzica.clear()
        if date[1] == 'house':
            await turn_context.send_activity(
                f"https://open.spotify.com/playlist/5OhjR3QIvNYUdsQVuJKWmu?si=c3cffc6715ae48d2")
            await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
            date.clear()
            muzica.clear()
        if date[1] == 'EDM':
            await turn_context.send_activity(
                f"https://open.spotify.com/playlist/5CvETxDs2E5rQeNji0LPaA?si=48d6671fabe246af")
            await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
            date.clear()
            muzica.clear()
        if date[1] == 'dubstep':
            await turn_context.send_activity(
                f"https://open.spotify.com/playlist/4WbwDAaDu7bzws8su8tACA?si=4f9d67998cb74397")
            await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
            date.clear()
            muzica.clear()


    elif text == 'artist':
        if date[1] == 'trap':
            artist.append('Lil Wayne')
            artist.append('Post Malone')
            await turn_context.send_activity(
                f"Pot sa-ti recomand artistii: Lil Wayne, Post Malone. Iti place careva dintre ei?")
        if date[1] == 'pop':
            artist.append('Drake')
            artist.append('Justin Bieber')
            await turn_context.send_activity(
                f"Pot sa-ti recomand artistii: Drake, Justin Bieber. Iti place careva dintre ei?")
        if date[1] == 'lo-fi':
            artist.append('Nujabes')
            artist.append('Beck')
            await turn_context.send_activity(f"Pot sa-ti recomand artistii: Nujabes, Beck. Iti place careva dintre ei?")
        if date[1] == 'sad music':
            artist.append('Billie Eilish')
            artist.append('Milky Chance')
            await turn_context.send_activity(
                f"Pot sa-ti recomand artistii: Milky Chance, Billie Eilish. Iti place careva dintre ei?")
        if date[1] == 'house':
            artist.append('David Guetta')
            artist.append('Diplo')
            await turn_context.send_activity(
                f"Pot sa-ti recomand artistii: David Guetta, Diplo. Iti place careva dintre ei?")
        if date[1] == 'EDM':
            artist.append('David Guetta')
            artist.append('Martin Garrix')
            await turn_context.send_activity(
                f"Pot sa-ti recomand artistii: David Guetta, Martin Garrix. Iti place careva dintre ei?")
        if date[1] == 'dubstep':
            artist.append('Skrillex')
            artist.append('Panda Eyes')
            await turn_context.send_activity(
                f"Pot sa-ti recomand artistii: Skrillex, Panda Eyes. Iti place careva dintre ei?")

    else:
        aux = " "
        for x in range(len(muzica)):
            aux = aux + muzica[x] + ", "
        await turn_context.send_activity(f"Nu ai ales nici un gen de care ti-am zis :(((."
                                         f"Eu am spus" + aux)


async def artisti(a, turn_context: TurnContext):
    if a == 'lil wayne':
        await turn_context.send_activity(
            f"Am un playlist de la lil wayne pregatit pentru tine: "
            f"https://open.spotify.com/playlist/1NNtf3CSyDBhNexSEqoQdm?si=7650b587c40c4c95")
        await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
        date.clear()
        muzica.clear()
    if a == 'post malone':
        await turn_context.send_activity(
            f"Am un playlist de la Post Malone pregatit pentru tine: "
            f"https://open.spotify.com/playlist/1jlgagZD8ZXkUFdIgYuz8m?si=71e01b0d75bc4052")
        await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
        date.clear()
        muzica.clear()
    if a == 'drake':
        await turn_context.send_activity(
            f"Am un playlist de la Drake pregatit pentru tine: "
            f"https://open.spotify.com/playlist/6PJa063pl5xkxnEVRkO9SL?si=cade77766b0e4027")
        await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
        date.clear()
        muzica.clear()
    if a == 'justin bieber':
        await turn_context.send_activity(
            f"Am un playlist de la Justin Bieber pregatit pentru tine: "
            f"https://open.spotify.com/playlist/3FxqCKNmp8J6so3EQW4RMt?si=62567b0df043425b")
        await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
        date.clear()
        muzica.clear()
    if a == 'nujabes':
        await turn_context.send_activity(
            f"Am un playlist de la Nujabes pregatit pentru tine: "
            f"https://open.spotify.com/playlist/37i9dQZF1DZ06evO2fAoGH?si=c9057baa29794b33")
        await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
        date.clear()
        muzica.clear()
    if a == 'beck':
        await turn_context.send_activity(
            f"Am un playlist de la Beck  pregatit pentru tine: "
            f"https://open.spotify.com/album/6BOQkxcHspMoRWEwEexf4l?si=yBJRu4vRSBW9xhrXzHvi4g")
        await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
        date.clear()
        muzica.clear()
    if a == 'billie eilish':
        await turn_context.send_activity(
            f"Am un playlist de la Billie Eilish  pregatit pentru tine: "
            f"https://open.spotify.com/playlist/37i9dQZF1DX6cg4h2PoN9y?si=40f64ac3e2a34b71")
        await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
        date.clear()
        muzica.clear()
    if a == 'milky chance':
        await turn_context.send_activity(
            f"Am un playlist de la Milky Chance pregatit pentru tine: "
            f"https://open.spotify.com/playlist/37i9dQZF1DXa0p5fNY1Mvw?si=5cb4f5d1a81e444f")
        await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
        date.clear()
        muzica.clear()
    if a == 'david guetta':
        await turn_context.send_activity(
            f"Am un playlist de la David Guetta pregatit pentru tine: "
            f"https://open.spotify.com/playlist/1DHhWaAzOTvZEG5vDHbHOD?si=975d7946d18c45bf")
        await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
        date.clear()
        muzica.clear()
    if a == 'diplo':
        await turn_context.send_activity(
            f"Am un playlist de la Diplo pregatit pentru tine: "
            f"https://open.spotify.com/playlist/37i9dQZF1DX4QSOvQofBAJ?si=f7d5d6ea00d34d8e")
        await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
        date.clear()
        muzica.clear()
    if a == 'martin garrix':
        await turn_context.send_activity(
            f"Am un playlist de la Martin Garrix pregatit pentru tine: "
            f"https://open.spotify.com/playlist/37i9dQZF1DX94qaYRnkufr?si=77af71eed7d546c3")
        await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
        date.clear()
        muzica.clear()
    if a == 'skrillex':
        await turn_context.send_activity(
            f"Am un playlist de la Skrillex pregatit pentru tine: "
            f"https://open.spotify.com/playlist/37i9dQZF1DWWj5zlML0Fin?si=effadd9690e9480b")
        await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
        date.clear()
        muzica.clear()
    if a == 'panda eyes':
        await turn_context.send_activity(
            f"Am un playlist de la Panda Eyes pregatit pentru tine: "
            f"https://open.spotify.com/playlist/37i9dQZF1DZ06evO2b8bgD?si=e9b2ccb000ea42d2")
        await turn_context.send_activity(f"Mai pot sa-ti recomand niste muzica daca iti schimbi starea de spirit.")
        date.clear()
        muzica.clear()


class MyBot(ActivityHandler):

    async def on_message_activity(self, turn_context: TurnContext):

        try:
            appId = '606dbc00-24c4-4f47-9af4-e0992e633784'
            prediction_key = 'ae04b9b1448746bca9678ff3f4f1578c'
            prediction_endpoint = 'https://first.cognitiveservices.azure.com/'
            utterance = turn_context.activity.text
            headers = {
            }
            params = {
                'query': utterance,
                'timezoneOffset': '0',
                'verbose': 'true',
                'show-all-intents': 'true',
                'spellCheck': 'false',
                'staging': 'false',
                'subscription-key': prediction_key
            }
            response = requests.get(f'{prediction_endpoint}luis/prediction/v3.0/apps/{appId}/slots/production/predict',
                                    headers=headers, params=params)

            # Display the results on the console.

            datePrimite = response.json()
            intentie = datePrimite['prediction']['topIntent']
            if intentie == 'None' or intentie == 'Greetings':
                entitate = None
            else:
                entitate = list(datePrimite['prediction']['entities'].keys())[0]
                if entitate == 'feelings':
                    f = datePrimite['prediction']['entities']['$instance']['feelings'][0]['text']
                elif entitate == 'artisti':
                    a = datePrimite['prediction']['entities']['$instance']['artisti'][0]['text']
            print('Intentie: ', intentie)
            print('Entitate: ', entitate)
            print('\n')
        except Exception as e:
            # Display the error string.
            print(f'{e}')

        if intentie == 'Greetings':
            date.clear()
            muzica.clear()
            await turn_context.send_activity("Salut! Sunt cel mai tare bot de muzica ever")
            await turn_context.send_activity("Cum te simti astazi?")

        if intentie == 'None':
            date.clear()
            muzica.clear()
            await turn_context.send_activity(f"Nu inteleg ce ai spus acolo :((. "
                                             f"Saluta-ma din nou daca vrei sa mai vorbesti cu mine")

        if intentie == 'Preferinte':
            await preferinte(datePrimite, turn_context)

        if intentie == 'Feelings':
            await feeling(f, turn_context)

        if intentie == 'Artisti':
            await artisti(a, turn_context)

        if intentie == 'Negare':
            await turn_context.send_activity(f"La cum te simti pot sa-ti recmand niste muzica: ")

        if turn_context.activity.text == 'mai vreau niste muzica':
            await turn_context.send_activity("Vrei un playlist sau artist?")
            date.clear()
