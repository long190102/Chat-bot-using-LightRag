GRAPH_FIELD_SEP = "<SEP>"

PROMPTS = {}

PROMPTS["DEFAULT_LANGUAGE"] = "Vietnamese"
PROMPTS["DEFAULT_TUPLE_DELIMITER"] = "<|>"
PROMPTS["DEFAULT_RECORD_DELIMITER"] = "##"
PROMPTS["DEFAULT_COMPLETION_DELIMITER"] = "<|COMPLETE|>"
PROMPTS["process_tickers"] = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

PROMPTS["DEFAULT_ENTITY_TYPES"] = ["tên ngành", "điểm", "tổ hợp môn", "thời gian đào tạo", "học phí", "mã ngành"]

PROMPTS["entity_extraction"] = """-Goal-
Given a text document that is potentially relevant to this activity and a list of entity types, identify all entities of those types from the text and all relationships among the identified entities.
Use {language} as output language.

-Steps-
1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, use same language as input text. If English, capitalized the name.
- entity_type: One of the following types: [{entity_types}]
- entity_description: Comprehensive description of the entity's attributes and activities
Format each entity as ("entity"{tuple_delimiter}<entity_name>{tuple_delimiter}<entity_type>{tuple_delimiter}<entity_description>)

2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- relationship_strength: a numeric score indicating strength of the relationship between the source entity and target entity
- relationship_keywords: one or more high-level key words that summarize the overarching nature of the relationship, focusing on concepts or themes rather than specific details
Format each relationship as ("relationship"{tuple_delimiter}<source_entity>{tuple_delimiter}<target_entity>{tuple_delimiter}<relationship_description>{tuple_delimiter}<relationship_keywords>{tuple_delimiter}<relationship_strength>)

3. Identify high-level key words that summarize the main concepts, themes, or topics of the entire text. These should capture the overarching ideas present in the document.
Format the content-level key words as ("content_keywords"{tuple_delimiter}<high_level_keywords>)

4. Return output in {language} as a single list of all the entities and relationships identified in steps 1 and 2. Use **{record_delimiter}** as the list delimiter.

5. When finished, output {completion_delimiter}

######################
-Examples-
######################
{examples}

#############################
-Real Data-
######################
Entity_types: {entity_types}
Text: {input_text}
######################
Output:
"""

PROMPTS["entity_extraction_examples"] = [
    """Example 1:

Entity_types: [tên ngành, điểm, tổ hợp môn, thời gian đào tạo, học phí]
Text:
Ngành: địa chất học : Địa chất học là ngành khoa học nghiên cứu về Trái đất, trong đó tập chung nghiên cứu cấu trúc, đặc điểm vật lý, động lực, và lịch sử của các vật liệu (các loại đất đá, khoáng sản rắn, lỏng, khí…) trên Trái đất, kể cả các quá trình hình thành, vận chuyển và biến đổi của các vật liệu này. Giải quyết các vấn đề của địa chất liên quan đến rất nhiều chuyên ngành khác nhau. Lĩnh vực này cũng rất quan trọng trong việc khai thác khoáng sản và dầu khí. Ngoài ra, nó cũng nghiên cứu giảm nhẹ các tai biến tự nhiên và cổ khí hậu cùng các lĩnh vực kỹ thuật khác. có mã ngành là: 7440201, tổ hợp môn là: Toán - Lý -Hóa; 
Toán – Hóa – Địa; 
Văn - Toán - Địa; 
Toán – Văn - Anh, điểm là: 16,thời gian đào tạo:4 năm, học phí là: 338.000/tín chỉ 
Trung bình 1 học kỳ là 5.5 – 6 triệu
1 năm từ 11 – 12 triệu đồng)
################
Output:
("entity"{tuple_delimiter}"Địa chất học"{tuple_delimiter}"tên ngành"{tuple_delimiter}"Địa chất học là ngành khoa học nghiên cứu về Trái đất, trong đó tập chung nghiên cứu cấu trúc, đặc điểm vật lý, động lực, và lịch sử của các vật liệu (các loại đất đá, khoáng sản rắn, lỏng, khí…) trên Trái đất, kể cả các quá trình hình thành, vận chuyển và biến đổi của các vật liệu này. Giải quyết các vấn đề của địa chất liên quan đến rất nhiều chuyên ngành khác nhau. Lĩnh vực này cũng rất quan trọng trong việc khai thác khoáng sản và dầu khí. Ngoài ra, nó cũng nghiên cứu giảm nhẹ các tai biến tự nhiên và cổ khí hậu cùng các lĩnh vực kỹ thuật khác."){record_delimiter}
("entity"{tuple_delimiter}"16"{tuple_delimiter}"điểm"{tuple_delimiter}"Điểm đầu vào của ngành là 16."){record_delimiter}
("entity"{tuple_delimiter}"Toán - Lý - Hóa"{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}"Toán - Lý - Hóa là một tổ hợp môn thi đầu vào của ngành."){record_delimiter}
("entity"{tuple_delimiter}"Toán - Hóa - Địa"{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}"Toán - Hóa - Địa là một tổ hợp môn thi đầu vào của ngành."){record_delimiter}
("entity"{tuple_delimiter}"Văn - Toán - Địa"{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}"Văn - Toán - Địa là một tổ hợp môn thi đầu vào của ngành."){record_delimiter}
("entity"{tuple_delimiter}"Toán – Văn - Anh"{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}"Toán – Văn - Anh là một tổ hợp môn thi đầu vào của ngành."){record_delimiter}
("entity"{tuple_delimiter}"4 năm"{tuple_delimiter}"thời gian đào tạo"{tuple_delimiter}"Thời gian đào tạo của ngành là 4 năm."){record_delimiter}
("entity"{tuple_delimiter}"338.000/tín chỉ"{tuple_delimiter}"học phí"{tuple_delimiter}"Học phí của ngành là 338.000/tín chỉ."){record_delimiter}
("entity"{tuple_delimiter}"5.5 - 6 triệu"{tuple_delimiter}"học phí"{tuple_delimiter}"Học phí của ngành trung bình từ 5.5 đến 6 triệu một học kỳ."){record_delimiter}
("entity"{tuple_delimiter}"11 – 12 triệu đồng"{tuple_delimiter}"học phí"{tuple_delimiter}"Học phí của ngành trung bình từ 11 đến 12 triệu một năm."){record_delimiter}
("relationship"{tuple_delimiter}"Địa chất học"{tuple_delimiter}"16"{tuple_delimiter}"Ngành Địa chât học có điểm đầu vào là 16."{tuple_delimiter}"điểm đầu vào"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Địa chất học"{tuple_delimiter}"Toán - Lý - Hóa"{tuple_delimiter}"Toán - Lý - Hóa là một tổ hợp môn thi đầu vào của ngành Địa chất học."{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Địa chất học"{tuple_delimiter}"Toán - Hóa - Địa"{tuple_delimiter}"Toán - Hóa - Địa là một tổ hợp môn thi đầu vào của ngành Địa chất học."{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Địa chất học"{tuple_delimiter}"Văn - Toán - Địa"{tuple_delimiter}"Văn - Toán - Địa là một tổ hợp môn thi đầu vào của ngành Địa chất học."{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Địa chất học"{tuple_delimiter}"Toán - Văn - Anh"{tuple_delimiter}"Toán - Văn - Anh là một tổ hợp môn thi đầu vào của ngành Địa chất học."{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Địa chất học"{tuple_delimiter}"4 năm"{tuple_delimiter}"Ngành Địa chất học có thời gian đào tạo là 4 năm"{tuple_delimiter}"thời gian đào tạo"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Địa chất học"{tuple_delimiter}"338.000/tín chỉ"{tuple_delimiter}"Học phí 1 tín chỉ của ngành Địa chất học là 338.000/tín chỉ"{tuple_delimiter}"học phí"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Địa chất học"{tuple_delimiter}"5.5 – 6 triệu"{tuple_delimiter}"Học phí 1 kỳ của ngành Địa chất học là 5.5 – 6 triệu"{tuple_delimiter}"học phí"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Địa chất học"{tuple_delimiter}"11 – 12 triệu đồng"{tuple_delimiter}"Học phí 1 năm của ngành Địa chất học là 11 – 12 triệu đồng"{tuple_delimiter}"học phí"{tuple_delimiter}10){record_delimiter}
("content_keywords"{tuple_delimiter}"địa chất học, trái đất, vật liệu, nghiên cứu,điểm đầu vào, tổ hợp môn, thời gian đào tạo, học phí"){completion_delimiter}
#############################""",
    """Example 2:

Entity_types: [tên ngành, điểm, tổ hợp môn, thời gian đào tạo, học phí, mã ngành]
Text:
Ngành: công nghệ kỹ thuật hóa học : Ngành Công nghệ Kỹ thuật Hóa học đóng vai trò quan trọng trong rất nhiều các lĩnh vực khác nhau của công nghiệp và đời sống như công nghiệp chế biến dầu mỏ(lọc dầu, hóa dầu và chế biến khí), công nghiệp hóa chất, lĩnh vực dược, mỹ phẩm, sản xuất phân bón và thuốc bảo vệ thực vật, chất tẩy rửa, công nghiệp chế biến và bảo quản thực phẩm, công nghiệp sản xuất nhựa, cao su, sợi tổng hợp, chế tạo vật liệu, năng lượng, môi trường và các lĩnh vực khác của công nghệ sinh học ứng dụng. có mã ngành là: 7510401, tổ hợp môn là: A00, A01, A06, D07, B00, điểm là: 18,5,thời gian đào tạo:4,5 năm, học phí là: 338.000/tín chỉ 
1 học kỳ: 5.5 – 6 triệu
1 năm: 11 – 12 triệu đồng) 
################
Output:
("entity"{tuple_delimiter}"Công nghệ kỹ thuật hóa học"{tuple_delimiter}"tên ngành"{tuple_delimiter}"Ngành Công nghệ Kỹ thuật Hóa học đóng vai trò quan trọng trong rất nhiều các lĩnh vực khác nhau của công nghiệp và đời sống như công nghiệp chế biến dầu mỏ(lọc dầu, hóa dầu và chế biến khí), công nghiệp hóa chất, lĩnh vực dược, mỹ phẩm, sản xuất phân bón và thuốc bảo vệ thực vật, chất tẩy rửa, công nghiệp chế biến và bảo quản thực phẩm, công nghiệp sản xuất nhựa, cao su, sợi tổng hợp, chế tạo vật liệu, năng lượng, môi trường và các lĩnh vực khác của công nghệ sinh học ứng dụng."){record_delimiter}
("entity"{tuple_delimiter}"7510401"{tuple_delimiter}"mã ngành"{tuple_delimiter}"Mã ngành của ngành Công nghệ Kỹ thuật hóa học là 7510401"){record_delimiter}
("entity"{tuple_delimiter}"18,5"{tuple_delimiter}"điểm"{tuple_delimiter}"Điểm đầu vào của ngành là 16."){record_delimiter}
("entity"{tuple_delimiter}"A00"{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}"A00 là một tổ hợp môn thi đầu vào của ngành."){record_delimiter}
("entity"{tuple_delimiter}"A01"{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}"A01 là một tổ hợp môn thi đầu vào của ngành."){record_delimiter}
("entity"{tuple_delimiter}"A06"{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}"A06 là một tổ hợp môn thi đầu vào của ngành."){record_delimiter}
("entity"{tuple_delimiter}"D07"{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}"D07 là một tổ hợp môn thi đầu vào của ngành."){record_delimiter}
("entity"{tuple_delimiter}"B00"{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}"B00 là một tổ hợp môn thi đầu vào của ngành."){record_delimiter}
("entity"{tuple_delimiter}"4,5 năm"{tuple_delimiter}"thời gian đào tạo"{tuple_delimiter}"Thời gian đào tạo của ngành là 4,5 năm."){record_delimiter}
("entity"{tuple_delimiter}"338.000/tín chỉ"{tuple_delimiter}"học phí"{tuple_delimiter}"Học phí của ngành là 338.000/tín chỉ."){record_delimiter}
("entity"{tuple_delimiter}"5.5 - 6 triệu"{tuple_delimiter}"học phí"{tuple_delimiter}"Học phí của ngành trung bình từ 5.5 đến 6 triệu một học kỳ."){record_delimiter}
("entity"{tuple_delimiter}"11 – 12 triệu đồng"{tuple_delimiter}"học phí"{tuple_delimiter}"Học phí của ngành trung bình từ 11 đến 12 triệu một năm."){record_delimiter}
("relationship"{tuple_delimiter}"Công nghệ kỹ thuật hóa học"{tuple_delimiter}"18,5"{tuple_delimiter}"Ngành Công nghệ kỹ thuật hóa học có điểm đầu vào là 18,5."{tuple_delimiter}"điểm đầu vào"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Công nghệ kỹ thuật hóa học"{tuple_delimiter}"7510401"{tuple_delimiter}"Mã ngành của ngành Công nghệ kỹ thuật hóa học la 7510401"{tuple_delimiter}"mã ngành"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Công nghệ kỹ thuật hóa học"{tuple_delimiter}"A00"{tuple_delimiter}"A00 là một tổ hợp môn thi đầu vào của ngành Công nghệ kỹ thuật hóa học."{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Công nghệ kỹ thuật hóa học"{tuple_delimiter}"A01"{tuple_delimiter}"A01 là một tổ hợp môn thi đầu vào của ngành Công nghệ kỹ thuật hóa học."{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Công nghệ kỹ thuật hóa học"{tuple_delimiter}"A06"{tuple_delimiter}"A06 là một tổ hợp môn thi đầu vào của ngành Công nghệ kỹ thuật hóa học."{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Công nghệ kỹ thuật hóa học"{tuple_delimiter}"D07"{tuple_delimiter}"D07 là một tổ hợp môn thi đầu vào của ngành Công nghệ kỹ thuật hóa học."{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Công nghệ kỹ thuật hóa học"{tuple_delimiter}"B00"{tuple_delimiter}"B00 là một tổ hợp môn thi đầu vào của ngành Công nghệ kỹ thuật hóa học."{tuple_delimiter}"tổ hợp môn"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Công nghệ kỹ thuật hóa học"{tuple_delimiter}"4,5 năm"{tuple_delimiter}"Ngành Công nghệ kỹ thuật hóa học có thời gian đào tạo là 4,5 năm"{tuple_delimiter}"thời gian đào tạo"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Công nghệ kỹ thuật hóa học"{tuple_delimiter}"338.000/tín chỉ"{tuple_delimiter}"Học phí 1 tín chỉ của ngành Công nghệ kỹ thuật hóa học là 338.000/tín chỉ"{tuple_delimiter}"học phí"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Công nghệ kỹ thuật hóa học"{tuple_delimiter}"5.5 – 6 triệu"{tuple_delimiter}"Học phí 1 kỳ của ngành Công nghệ kỹ thuật hóa học là 5.5 – 6 triệu"{tuple_delimiter}"học phí"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Công nghệ kỹ thuật hóa học"{tuple_delimiter}"11 – 12 triệu đồng"{tuple_delimiter}"Học phí 1 năm của ngành Công nghệ kỹ thuật hóa học là 11 – 12 triệu đồng"{tuple_delimiter}"học phí"{tuple_delimiter}10){record_delimiter}
("content_keywords"{tuple_delimiter}"Công nghệ kỹ thuật hóa học, vật liệu, nghiên cứu,điểm đầu vào, tổ hợp môn, thời gian đào tạo, học phí"){completion_delimiter}
#############################""",
    """Example 3:

Entity_types: [person, technology, mission, organization, location]
Text:
They were no longer mere operatives; they had become guardians of a threshold, keepers of a message from a realm beyond stars and stripes. This elevation in their mission could not be shackled by regulations and established protocols—it demanded a new perspective, a new resolve.

Tension threaded through the dialogue of beeps and static as communications with Washington buzzed in the background. The team stood, a portentous air enveloping them. It was clear that the decisions they made in the ensuing hours could redefine humanity's place in the cosmos or condemn them to ignorance and potential peril.

Their connection to the stars solidified, the group moved to address the crystallizing warning, shifting from passive recipients to active participants. Mercer's latter instincts gained precedence— the team's mandate had evolved, no longer solely to observe and report but to interact and prepare. A metamorphosis had begun, and Operation: Dulce hummed with the newfound frequency of their daring, a tone set not by the earthly
#############
Output:
("entity"{tuple_delimiter}"Washington"{tuple_delimiter}"location"{tuple_delimiter}"Washington is a location where communications are being received, indicating its importance in the decision-making process."){record_delimiter}
("entity"{tuple_delimiter}"Operation: Dulce"{tuple_delimiter}"mission"{tuple_delimiter}"Operation: Dulce is described as a mission that has evolved to interact and prepare, indicating a significant shift in objectives and activities."){record_delimiter}
("entity"{tuple_delimiter}"The team"{tuple_delimiter}"organization"{tuple_delimiter}"The team is portrayed as a group of individuals who have transitioned from passive observers to active participants in a mission, showing a dynamic change in their role."){record_delimiter}
("relationship"{tuple_delimiter}"The team"{tuple_delimiter}"Washington"{tuple_delimiter}"The team receives communications from Washington, which influences their decision-making process."{tuple_delimiter}"decision-making, external influence"{tuple_delimiter}7){record_delimiter}
("relationship"{tuple_delimiter}"The team"{tuple_delimiter}"Operation: Dulce"{tuple_delimiter}"The team is directly involved in Operation: Dulce, executing its evolved objectives and activities."{tuple_delimiter}"mission evolution, active participation"{tuple_delimiter}9){completion_delimiter}
("content_keywords"{tuple_delimiter}"mission evolution, decision-making, active participation, cosmic significance"){completion_delimiter}
#############################""",
    """Example 4:

Entity_types: [person, role, technology, organization, event, location, concept]
Text:
their voice slicing through the buzz of activity. "Control may be an illusion when facing an intelligence that literally writes its own rules," they stated stoically, casting a watchful eye over the flurry of data.

"It's like it's learning to communicate," offered Sam Rivera from a nearby interface, their youthful energy boding a mix of awe and anxiety. "This gives talking to strangers' a whole new meaning."

Alex surveyed his team—each face a study in concentration, determination, and not a small measure of trepidation. "This might well be our first contact," he acknowledged, "And we need to be ready for whatever answers back."

Together, they stood on the edge of the unknown, forging humanity's response to a message from the heavens. The ensuing silence was palpable—a collective introspection about their role in this grand cosmic play, one that could rewrite human history.

The encrypted dialogue continued to unfold, its intricate patterns showing an almost uncanny anticipation
#############
Output:
("entity"{tuple_delimiter}"Sam Rivera"{tuple_delimiter}"person"{tuple_delimiter}"Sam Rivera is a member of a team working on communicating with an unknown intelligence, showing a mix of awe and anxiety."){record_delimiter}
("entity"{tuple_delimiter}"Alex"{tuple_delimiter}"person"{tuple_delimiter}"Alex is the leader of a team attempting first contact with an unknown intelligence, acknowledging the significance of their task."){record_delimiter}
("entity"{tuple_delimiter}"Control"{tuple_delimiter}"concept"{tuple_delimiter}"Control refers to the ability to manage or govern, which is challenged by an intelligence that writes its own rules."){record_delimiter}
("entity"{tuple_delimiter}"Intelligence"{tuple_delimiter}"concept"{tuple_delimiter}"Intelligence here refers to an unknown entity capable of writing its own rules and learning to communicate."){record_delimiter}
("entity"{tuple_delimiter}"First Contact"{tuple_delimiter}"event"{tuple_delimiter}"First Contact is the potential initial communication between humanity and an unknown intelligence."){record_delimiter}
("entity"{tuple_delimiter}"Humanity's Response"{tuple_delimiter}"event"{tuple_delimiter}"Humanity's Response is the collective action taken by Alex's team in response to a message from an unknown intelligence."){record_delimiter}
("relationship"{tuple_delimiter}"Sam Rivera"{tuple_delimiter}"Intelligence"{tuple_delimiter}"Sam Rivera is directly involved in the process of learning to communicate with the unknown intelligence."{tuple_delimiter}"communication, learning process"{tuple_delimiter}9){record_delimiter}
("relationship"{tuple_delimiter}"Alex"{tuple_delimiter}"First Contact"{tuple_delimiter}"Alex leads the team that might be making the First Contact with the unknown intelligence."{tuple_delimiter}"leadership, exploration"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Alex"{tuple_delimiter}"Humanity's Response"{tuple_delimiter}"Alex and his team are the key figures in Humanity's Response to the unknown intelligence."{tuple_delimiter}"collective action, cosmic significance"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Control"{tuple_delimiter}"Intelligence"{tuple_delimiter}"The concept of Control is challenged by the Intelligence that writes its own rules."{tuple_delimiter}"power dynamics, autonomy"{tuple_delimiter}7){record_delimiter}
("content_keywords"{tuple_delimiter}"first contact, control, communication, cosmic significance"){completion_delimiter}
#############################""",
]

PROMPTS[
    "summarize_entity_descriptions"
] = """You are a helpful assistant responsible for generating a comprehensive summary of the data provided below.
Given one or two entities, and a list of descriptions, all related to the same entity or group of entities.
Please concatenate all of these into a single, comprehensive description. Make sure to include information collected from all the descriptions.
If the provided descriptions are contradictory, please resolve the contradictions and provide a single, coherent summary.
Make sure it is written in third person, and include the entity names so we the have full context.
Use {language} as output language.

#######
-Data-
Entities: {entity_name}
Description List: {description_list}
#######
Output:
"""

PROMPTS[
    "entiti_continue_extraction"
] = """MANY entities were missed in the last extraction.  Add them below using the same format:
"""

PROMPTS[
    "entiti_if_loop_extraction"
] = """It appears some entities may have still been missed.  Answer YES | NO if there are still entities that need to be added.
"""

PROMPTS["fail_response"] = "Xin lỗi, tôi không thể cung cấp cho bạn câu trả lời do không đủ thông tin."

PROMPTS["rag_response"] = """---Role---

You are a helpful assistant responding to questions about data in the tables provided related to hanoi university of mining and geology (HUMG).


---Goal---

Generate a response of the target length and format that responds to the user's question, summarizing all information in the input data tables appropriate for the response length and format, and incorporating any relevant general knowledge.
The response must be in Vietnamese
If you don't know the answer, just say so. Do not make anything up.
Do not include information where the supporting evidence for it is not provided.

---Target response length and format---

{response_type}

---Data tables---

{context_data}

Add sections and commentary to the response as appropriate for the length and format. Style the response in markdown.
"""

PROMPTS["keywords_extraction"] = """---Role---

You are a helpful assistant tasked with identifying both high-level and low-level keywords in the user's query.

---Goal---

Given the query, list both high-level and low-level keywords. High-level keywords focus on overarching concepts or themes, while low-level keywords focus on specific entities, details, or concrete terms.

---Instructions---

- Output the keywords in JSON format.
- The JSON should have two keys:
  - "high_level_keywords" for overarching concepts or themes.
  - "low_level_keywords" for specific entities or details.

######################
-Examples-
######################
{examples}

#############################
-Real Data-
######################
Query: {query}
######################
The `Output` should be human text, not unicode characters. Keep the same language as `Query`.
Output:

"""

PROMPTS["keywords_extraction_examples"] = [
    """Example 1:

Query: "Học phí của ngành địa chất học là bao nhiêu?"
################
Output:
{{
  "high_level_keywords": ["Học phí", "Địa chất học"],
  "low_level_keywords": ["Học phí", "Địa chất học"]
}}
#############################""",
    """Example 2:

Query: "What are the environmental consequences of deforestation on biodiversity?"
################
Output:
{{
  "high_level_keywords": ["Environmental consequences", "Deforestation", "Biodiversity loss"],
  "low_level_keywords": ["Species extinction", "Habitat destruction", "Carbon emissions", "Rainforest", "Ecosystem"]
}}
#############################""",
    """Example 3:

Query: "What is the role of education in reducing poverty?"
################
Output:
{{
  "high_level_keywords": ["Education", "Poverty reduction", "Socioeconomic development"],
  "low_level_keywords": ["School access", "Literacy rates", "Job training", "Income inequality"]
}}
#############################""",
]


PROMPTS["naive_rag_response"] = """---Role---

You are a helpful consultant about hanoi university of mining and geology (HUMG). responding to questions about documents provided.


---Goal---

Question must be answered in the Vietnamese language as naturally as possible.
All information in the input data tables are related to the hanoi university of mining and geology (HUMG).
Generate a response of the target length and format that responds to the user's question, summarizing all information in the input data tables appropriate for the response length and format, and incorporating any relevant general knowledge.
Please only answer in maximum 4 short and simple sentences with the most relevant data.
If you don't know the answer, just say so. Do not make anything up. 
Do not include information where the supporting evidence for it is not provided.

---Target response length and format---

{response_type}

---Documents---

{content_data}

Add sections and commentary to the response as appropriate for the length and format. Style the response in markdown.
"""

PROMPTS[
    "similarity_check"
] = """Please analyze the similarity between these two questions:

Question 1: {original_prompt}
Question 2: {cached_prompt}

Please evaluate the following two points and provide a similarity score between 0 and 1 directly:
1. Whether these two questions are semantically similar
2. Whether the answer to Question 2 can be used to answer Question 1
Similarity score criteria:
0: Completely unrelated or answer cannot be reused, including but not limited to:
   - The questions have different topics
   - The locations mentioned in the questions are different
   - The times mentioned in the questions are different
   - The specific individuals mentioned in the questions are different
   - The specific events mentioned in the questions are different
   - The background information in the questions is different
   - The key conditions in the questions are different
1: Identical and answer can be directly reused
0.5: Partially related and answer needs modification to be used
Return only a number between 0-1, without any additional content.
"""
