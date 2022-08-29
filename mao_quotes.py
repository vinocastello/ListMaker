import random

quotes = [
    "A revolution is not a dinner party, or writing an essay, or painting a picture, or doing embroidery; it cannot be so refined, so leisurely and gentle, so temperate, kind, courteous, restrained and magnanimous. A revolution is an insurrection, an act of violence by which one class overthrows another.",
    "When we look at a thing, we must examine its essence and treat its appearance merely as an usher at the threshold, and once we cross the threshold, we must grasp the essence of the thing; this is the only reliable and scientific method of analysis.",
    "The revolutionary war is a war of the masses; only mobilizing the masses and relying on them can wage it.",
    "In approaching a problem a Marxist should see the whole as well as the parts. A frog in a well says, “The sky is no bigger than the mouth of the well.” That is untrue, for the sky is not just the size of the mouth of the well. If it said, “A part of the sky is the size of the mouth of a well”, that would be true, for it tallies with the facts.",
    "It is well known that when you do anything, unless you understand its actual circumstances, its nature and its relations to other things, you will not know the laws governing it, or know how to do it, or be able to do it well.",
    "War is the highest form of struggle for resolving contradictions, when they have developed to a certain stage, between classes, nations, states, or political groups, and it has existed ever since the emergence of private property and of classes.",
    "What we need is an enthusiastic but calm state of mind and intense but orderly work.",
    "Communists should be the most farsighted, the most self-sacrificing, the most resolute, and the least prejudiced in sizing up situations, and should rely on the majority of the masses and win their support.",
    "In class society, everyone lives as a member of a particular class, and every kind of thinking, without exception, is stamped with the brand of a class.",
    "If we have a correct theory but merely prate about it, pigeonhole it and do not put it into practice, then that theory, however good, is of no significance.",
    "Marxist philosophy holds that the most important problem does not lie in understanding the laws of the objective world and thus being able to explain it, but in applying the knowledge of these laws actively to change the world.",
    "The fundamental cause of the development of a thing is not external but internal; it lies in the contradictoriness within the thing. This internal contradiction exists in every single thing, hence its motion and development. Contradictoriness within a thing is the fundamental cause of its development, while its interrelations and interactions with other things are secondary causes.",
    "The army must become one with the people so that they see it as their own army. Such an army will be invincible....",
    "Communists should set an example in being practical as well as far-sighted. For only by being practical can they fulfil the appointed tasks, and only far-sightedness can prevent them from losing their bearings in the march forward.",
    "Communists should set an example in study; at all times they should be pupils of the masses as well as their teachers.",
    "Every Communist working in the mass movements should be a friend of the masses and not a boss over them, an indefatigable teacher and not a bureaucratic politician.",
    "The attitude of Communists towards any person who has made mistakes in his work should be one of persuasion in order to help him change and start afresh and not one of exclusion, unless he is incorrigible.",
    "As for people who are politically backward, Communists should not slight or despise them, but should befriend them, unite with them, convince them and encourage them to go forward.",
    "The theory of Marx, Engels, Lenin and Stalin is universally applicable. We should regard it not as a dogma, but as a guide to action. Studying it is not merely a matter of learning terms and phrases but of learning Marxism-Leninism as the science of revolution.",
    "Every Communist must grasp the truth; “Political power grows out of the barrel of a gun.”",
    "Revolutionary culture is a powerful revolutionary weapon for the broad masses of the people. It prepares the ground ideologically before the revolution comes and is an important, indeed essential, fighting front in the general revolutionary front during the revolution.",
    "The masses are the real heroes, while we ourselves are often childish and ignorant, and without this understanding, it is impossible to acquire even the most rudimentary knowledge.",
    "The people, and the people alone, are the motive force in the making of world history.",
    "Without a People's army, the people have nothing.",
    "All reactionaries are paper tigers. In appearance, the reactionaries are terrifying, but in reality, they are not so powerful. From a long-term point of view, it is not the reactionaries but the people who are powerful.",
    "The People's democratic dictatorship needs the leadership of the working class. For it is only the working class that is most far-sighted, most selfless and most thoroughly revolutionary. The entire history of revolution proves that without the leadership of the working class revolution fails and that with the leadership of the working class revolution triumphs.",
    "The People's democratic dictatorship is based on the alliance of the working class, the peasantry and the urban petty bourgeoisie, and mainly on the alliance of the workers and the peasants.",
    "Two types of social contradictions - those between ourselves and the enemy and those among the people themselves confront us. The two are totally different in their nature.",
    "Communists must use the democratic method of persuasion and education when working among the laboring people and must on no account resort to commandism or coercion. The Chinese Communist Party faithfully adheres to this Marxist-Leninist principle.",
    "It is man's social being that determines his thinking. Once the correct ideas characteristic of the advanced class are grasped by the masses, these ideas turn into a material force which changes society and changes the world.",
    "Where do correct ideas come from? Do they drop from the skies? No. Are they innate in the mind? No. They come from social practice and from it alone. They come from three kinds of social practice: the struggle for production, the class struggle and scientific experiment.",
    "We must learn to look at problems all-sidedly, seeing the reverse as well as the obverse side of things. In given conditions, a bad thing can lead to good results and a good thing to bad results."

]

def get_quote():
    return f"`{random.choice(quotes)}`"

cat_commands = {"cat","cats","catto","cattos","mao","meow","pusa"}