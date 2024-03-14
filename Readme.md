# Pruebas de lectura de carteles
## Descripción de cartel
Prompt: `What’s in this image?`

![Cartel limpieza barranco](https://temporal.garimbaboy.com/barranco.jpeg)

>The image appears to be a promotional poster or flyer for an environmental cleanup event. The text at the top reads "Limpieza del Barranco Amargavinos," which translates to "Cleaning of the Amargavinos Ravine." Below that is a cartoon illustration of a person crouching down and picking up trash such as bottles and papers, placing it into a black trash bag. The illustration style is simple and colorful.
>
>Additional details on the poster announce the date and time of the event as "SÁBADO, 16 DE MARZO 2024" (Saturday, March 16, 2024), and the location "PLAZA DE LAS MADRES, SAN JOSÉ" at "9:30 HORAS" (9:30 AM). There's a logo at the bottom with the text "Breña Baja" and a slogan "SIENTE LA MAGIA DE UN LUGAR ÚNICO" which means "FEEL THE MAGIC OF A UNIQUE PLACE." This suggests that the event is organized in Breña Baja, which might be a town or city. The overall message is encouraging community involvement in an environmental cleanup.

![Cartel Forestarock](https://temporal.garimbaboy.com/forestarock.jpeg)

>This image appears to be a poster for an event titled "PUNKTAGORDA FORESTA ROCK," set to take place on Saturday, April 20, 2024. The event is being held at the "Mercadillo de Puntagorda" with free entry, starting at 15:00 hrs. The poster lists several activities and features, such as:
>
>- Workshops ("Talleres") with proposals for a more habitable world, including eco-painting, collage, literary recycling, and eco-plasticine, as well as a DJ workshop for young people with "Pimienta Selectoras."
>- Information stands ("Stands Informativos") from various ecological and sustainable organizations and initiatives.
>- At 19:00 hrs, there is a mention of a manifesto from the "MVTO ECOLOGISTA ISLA DE LA PALMA."
>- There will be local products and beverages available, including beer, wine, and rum from specific brands, and food from "CFGMCocina y Pasteleria de Puntagorda." The proceeds are intended for projects related to agroecology, invasive species control, education, and land defense.
>- Starting at 19:30 hrs, there will be performances by music groups or artists, hinted by the names at the bottom: "Babani Kone," "Las Ratas," "Tensö," and "Monte Reina."
>
>The poster uses a color scheme of red, white

## Prompt de tabulación v0.0.0

| Attribute   | Value                                          |
|-------------|------------------------------------------------|
| name        | PUNKTAGORDA Foresta Rock                       |
| date        | Saturday, April 20, 2024                       |
| location    | Mercadillo de Puntagorda                       |
| organizer   | Not explicitly stated, sponsors below the poster |
| category    | music, workshop, ecologism, rock               |
| other       | Free entry. Starts at 3:00 PM. Workshops on eco painting, recycling, DJ workshop for youths. Stands from various ecological and energy groups. Manifesto by Eco Movement of La Palma Island at 7:00 PM. Local food and beverages to support agroecology and territorial defense projects. Event features bands Babanú and Las Ratas, as well as Monte Reina. |

Tabula bastante bien, se podría pulir algunos detalles como el formato de fecha o la ubicación por municipio.
La ubicación puede pulirse con un servidor [Nominatim](https://nominatim.org/) o alguna api de mapas.

A priori el mayor problema que le veo es que a veces **lee mal los logos**, pero sigue siendo bastante funcional.
