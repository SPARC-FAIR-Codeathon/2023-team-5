<p align="center">
    <img src="logo.png" alt="Logo" height="80">
  <br/>
  <h3 align="center">
  Chat with SPARC datasets</h3>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About](#about)
- [Problem Statement](#problem-statement)
- [Our Proposed Solution](#our-proposed-solution)
- [Workflow](#workflow)
- [Reporting issues](#reporting-issues)
- [FAIR practices](#fair-practices)
- [License](#license)
- [Team Members](#team-members)
- [Acknowledgements](#acknowledgements)

# About

This repository belongs to Team #5, **SPARC CHAT**, who took part in the [SPARC](https://commonfund.nih.gov/sparc) [Codeathon](https://sparc.science/news-and-events/events/2023sparc-codeathon/event-details) 2023. The project's concept and planning were collaboratively formulated by the team members during the event, reaching a mutual agreement.

# Problem Statement

For a new user, navigating unfamiliar resources like SPARC and its associated portals can be quite challenging, especially when trying to find specific information quickly. The process might involve extensive exploration, leading to significant time and effort being spent to acquire relevant information or datasets. In some cases, users may find themselves repeatedly searching for the same things in a never-ending loop. To achieve their purpose, users often need to search through various sections, projects, and pipelines, which can become a time-consuming task.

# Our Proposed Solution

The emergence of [OpenAI ChatGPT](https://chat.openai.com) marks a significant advancement in chatbot technology. This next-generation chatbot enables users to interactively and efficiently ask queries and receive relevant answers. However, it is essential to exercise caution while using it. OpenAI ChatGPT is a large language model (LLM) trained on extensive datasets gathered from the internet. Since its launch, numerous closed and [open-source](https://github.com/eugeneyan/open-llms) LLMs have also been released.

In this project, we leverage open-source LLMs and the available data on the SPARC portal to create a chatbot that assists users in finding the desired links and provides summaries of relevant information. Currently, the chatbot is limited to processing text-based information.

# Workflow

<p align="center">
    <img src="pipeline.png" alt="Pipeline" width="100%">
</p>

## Data

We gathered data from various pages of the SPARC portal, including the [SPARC Data & Models](https://sparc.science/data?type=dataset) page and other provided web links. For our model training, we randomly picked 12 datasets that contain valuable information related to related datasets, descriptions, abstracts, protocols, and other relevant details.

## Data pre-processing

After collecting the data, we subjected it to preprocessing using OpenAI ChatGPT, converting it into prompts and corresponding answers. The preprocessed data was then utilized to train our models.

## Model and Model Training

The collected data were preprocessed using [OpenAI ChatGPT](https://chat.openai.com/) and converted into prompts and answers. This data was used to train our models.

## Deployment

In order to ensure the model's accessibility and usability for users, Python language APIs were implemented and made available through Django. Users can access the model either via a web page or through the command line.

## Running the app

# Reporting issues

Please report an issue or suggest a new feature using the [issue page](https://github.com/SPARC-FAIR-Codeathon/2023-team-5/issues). Check existing issues before submitting a new one.

# FAIR practices

Since the codeathon focused on FAIR data principles, it was essential to ensure that the development of SPARC CHAT also adheres to FAIR principles.

# Team Members

- [Alireza Moshayedi](https://github.com/alrzmshy)[Lead]
- [Jialin](https://github.com/jlin95)[System Engineer]

- [Anmol Kiran](https://github.com/codemeleon)(Writer- Documentation)

# License

This code is licensed under the [MIT License](https://opensource.org/licenses/MIT).

- We can change it to another license if we need.

# Acknowledgements

We would like to thank the organizers of the SPARC Codeathon 2023 for guidance and help during this Codeathon.

# TODO

- [ ] FAIR practices statement for this project
