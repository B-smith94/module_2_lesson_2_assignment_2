attendees = int(input("Enter number of attendees: ")) #added int() to variable to indicate that the input should convert to an integer
venue = "large hall" if attendees > 100 else "conference room"
audio_system = "no audio system needed" if venue == "conference room" else "Big speakers"
projector = "large projector screen" if venue == "large hall" else "small projector"

print(venue)
print(audio_system)
print(projector)

food_type = input("Type of food (Vegitarian/non-vegitarian): ")
catering = input("Veggie Delight Caterers" if food_type == "vegitarian" else "Gourmet Meals Caterers")