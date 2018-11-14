# Security as Code

Hi, if you ended up here, sorry.. I really do.  As a geek and developer, I do not like to document things, nevertheless,  I think that this is a good opportunity to share the knowledge that I’ve acquired along the last years thanks to different specialists and resources that I’ve found on the internet.
Keep in mind that the assets within this repository has been compiled and modified according to my needs. I’ll try to document everything, but won’t be that hard to understand what we are trying to accomplish.
Finally, the main goal is to provide a proof of concept, we are not seeking to replace the current incident and management response tools and strategy deployed at your organization, but complement what you already have.


## Getting Started
Machine Learning is a transformational technology that have been here for years, but now thanks to the computational capabilities is easier for companies and community develop intelligent agents such as chatbots, intelligent cars or recommendation algorithms such as the one that Amazon or Netflix use.
For this particular proof of concept we will leverage AWS services  along with Gitlab CI/CD capabilities.

### Prerequisites
We will need the following items to partially or fully complete the PoC
* An AWS account  (The one with free tiers works)
* Basic knowledge on AWS services
* GitLab account
* Basic Python Knowledge
* Understand CI/CD and its benefits

### Setting up AWS account
We won’t go through all the details on how to create or harden an AWS account. You can find further information [Here](https://aws.amazon.com/es/iam/)

* Open the AWS console and in the services search bar type IAM
* Once there, select "users" in the menu bar located at the right of the screen and add a new user

![Add User](./img/addUser.png)


* Add a new user and check the "Programmatic account" box

![User Setting](./img/programaticAccount.png)


* For this PoC purposes give S3 and Lambda full access. Once created keep the Access Key and Secret Key information, we will use those two items when configuring our pipelines in GitLab


And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests
Explain how to run the automated tests for this system

### Break down into end to end tests
Explain what these tests test and why

```
Give an example
```

### And coding style tests
Explain what these tests test and why

```
Give an example
```

## Deployment
Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing
Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* *Billie Thompson* - /Initial work/ - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

