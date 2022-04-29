to obtain comment:
https://seekingalpha.com/api/v3/articles/4504702/comments?comment_ids[]=92188969&comment_ids[]=92188851&comment_ids[]=92188404&comment_ids[]=92185375&include=user&sort=-top_parent_id
note : articles/$nbr$ nbr is the id of the article, same as with the path of the earning call transcript
	obtainable from the api ask from url scrapping, it is called id in the metadata of script
to obtain comments id of all the page:
https://seekingalpha.com/api/v3/articles/4504702/comment_maps?include=user&sort=-top_parent_id

To recap:
https://seekingalpha.com/api/v3/articles/$id of the earning call$/comment_maps?include=user&sort=-top_parent_id
We get list of most recent comments id. We can now ask for the comments data.
https://seekingalpha.com/api/v3/articles/4504702/comments?comment_ids=$comment_id_1$,$comment_id_2$,$comment_id_3$
We get list of most recent comments.