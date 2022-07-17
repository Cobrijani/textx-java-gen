# textx-java-gen
Creating domain logic using textx and generating java code from it.

# Description
The purpose of this repository is to tryout the [textx](http://textx.github.io/textX/) dsl and to try to create an app from it, and trying to deduce 
from it how to model the language so that the domain logic can be solely designed using dsl and implementation logic using java and spring boot.

# Development checklist
- [ ] Develop language (*.mdl) for describing the entities and relationship between domain entities.
- [ ] Generate POJOs from Domain Language
- [ ] Develop language for describing backend logic such as REST Api, Database Logic etc.
- [ ] Generate Spring Boot backend based on Backend language
- [ ] Develop Language to describe Frontend behaviour
- [ ] Generate Angular app based ont Frontend language


# Personal Goal
To find out how efficient can DSLs be into developing applications where business logic is communicated through a custom language instead of embedding it dirrectly into Code.
Often the requirements are communicated to developers through different kind of documenting tools such as Confluence, Word and it would be nice that this knowledge is directly communicated through a custom defined language so transfer of knowledge is not likely prone to errors.
