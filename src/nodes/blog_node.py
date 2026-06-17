from src.states.blogstate import BlogState





class BlogNode:
    """
    A class to represnt blog node
    """

    def __init__(self,llm):
        self.llm = llm


    def title_creation(self,state:BlogState):
        """
        create the title for the blog
        """

        if "topic" in state and state["topic"]:
            promot = """ 
                     you are an expert blog content writer. Use markdown formatting. Genrate a blog title for the {topic}. This title should be creative and SEO firendly.


                     """
            
            system_message=promot.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog":{"title":response.content}}
        
    def content_generation(self,state=BlogState):
            promot = """ 
                     you are an expert blog blog writer. Use markdown formatting. Genrate a detailed blog contentwith detailed breakdown for the {topic}.


                     """
            
            system_message=promot.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog":{"title":state["blog"]["title"],"content": response.content}}

        
        