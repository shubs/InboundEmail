# InboundEmail
This is a project to handle automatically inbound email using mailjet API


				GetResults
					^|
					||
					|v
				 GAMESERVER(Button) -------SendAPI(Question)----ParseAPI---POST----> FLASKSERVER*(FIREBASE /game)
					^
					|
					|
		PUSH(FIREBASE /mail + /game)
					^|
					||
					|v
[MAIL] --POST--> FLASKSERVER
					^|
					||
					|v
				GET(MAILlist)

# Game server

@GET /
Listing de tout les resultats Question + 

Button to send the question (this will add the question ID to the question list on firebase) and put a trigger on "Waiting")
