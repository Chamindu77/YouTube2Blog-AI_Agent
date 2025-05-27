from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer

## Research Task
research_task = Task(
  description=(
    "Identify the video {topic}."
    "Get detailed information about the video from the channel video."
  ),
  expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
  tools=[yt_tool],
  agent=blog_researcher,
)

# Writing task 
write_task = Task(
  description=(
    "get the info from the youtube channel on the topic {topic}."
  ),
  expected_output='Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog',
  tools=[yt_tool],
  agent=blog_writer,
  async_execution=False,
  output_file='new-blog-post.md'  
)



# research_task = Task(
#     description=(
#         "Search for the topic {topic} on the provided YouTube channel."
#         " Extract any relevant details or transcriptions."
#     ),
#     expected_output='A detailed 3-paragraph summary of the video content.',
#     tools=[yt_tool],
#     agent=blog_researcher,
# )

# write_task = Task(
#     description=(
#         "Using the information from the research, write a blog post about the topic: {topic}."
#     ),
#     expected_output='A well-written blog post based on the researched video content.',
#     tools=[yt_tool],
#     agent=blog_writer,
#     async_execution=False,
#     output_file='new-blog-post.md'
# )


