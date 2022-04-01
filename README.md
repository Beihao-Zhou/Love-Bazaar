# Love-Bazaar
## Inspiration
As in previous years, the majority of donations came from individuals, accounting for 70% of all giving (https://www.charitynavigator.org/index.cfm?bay=content.view&cpid=42). This is understandable since the accumulation of small amounts of money can lead to an amazing number. Under such circumstances, how can we engage more people in the fundraising activity? Some people may have the willingness to support but think their donation is too small and “useless” and just give up. However, the amount of money is not that important! We may even help you reach your goals and engage your donors without any extra expenditure!
My idea is that there could be an online fundraising app out there to run a charity bazaar constantly. People can not only donate goods that they don’t need anymore to sell at the bazaar, but they can also purchase goods that had been donated by other individuals, with some items being purchased and donated cyclically. As a result, the platform can partner with charities and non-profit organizations and make sure the donations go to the appropriate place, ensuring charity accountability. 

## What it does
Love Bazaar is a web app that provides each individual with opportunities to engage with donors. In the platform, people can post their unused goods to sell, and all of the money earned by sales would contribute to their donations. Meanwhile, buying goods is also encouraged since every time you purchase, you actually donate your money to charities. 
The platform also provides users with good experiences when purchasing and selling. Individuals can just search for products by keywords. There are many categories of goods that can also help users filter products. Besides, people can also post their goods by filling in the necessary information of the goods, i.e. name, category, price, quantity available, photos. Moreover, users are allowed to add products to their shopping carts without logging in until they wish to check out at last. 

## How I built it
The front-end part of this full-stack web app is developed using Vue.js, and the design is completed by bulma library. Meanwhile, I implemented the back-end using Django linked with sqlite3 to fetch and post data. I designed and developed models, serializers, and API for products and orders of users. Users are authenticated and authorized through the Django REST framework. Furthermore, online payment is processed using Stripe. 

## Challenges that I ran into
When I developed the feature that allows users to post the image of their products, I encountered the problem that images cannot be sent to the backend. The first reason for the bug is that I submit JSON format information to the backend. This works for other data types except for File. After I changed the data into FormData, the backend succeeded in fetching the ImageFile. Moreover, the design of the API for saving images in the database is also different from other data types. Specifically, MultiPartParser and FormParser have to be overridden to deal with ImageFile. 

## Accomplishments that I'm proud of
- Successfully created this full stack web application that can transfer money
- Managed to create a fundraising app in a form of charity bazaar that can deal with the real-world problem

## What I learned
- Used Django REST framework to process users’ authentication and authorization
- Created models, serializers and API for products and orders using Django REST framework
- Processed online money payment using Stripe, securing users’ private information
- Allowed users to add items to shopping cart using state of Vue, along with localStorage

## What's next for Love Bazaar
Currently, the platform decides where the donations go after users’ payment. However, each non-profit and charity may have their own missions and visions, which means users may prefer one to another because of this. One idea is that users can choose their favorite organizations to donate, which can probably encourage them to engage in the community more actively. Therefore, a page that introduces the sponsors and partners should be added, and a selection box, which includes all organizations should be included when posting goods
