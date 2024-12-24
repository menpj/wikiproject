Designed a Wikipedia-like online encyclopedia. Project is implemented using Django HTML and Markdown.
Stored encyclopedia entries using a markup language called Markdown. 

Entry Page: Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, renders a page that displays the contents of that entry.

Search: Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.

If the query matches the name of an encyclopedia entry, the user will be redirected to that entry’s page.
If the query does not match the name of an entry, the user is instead taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python should appear in the search results. Clicking on any of the entry names on the search results page takes the user to that entry’s page.

New Page: Clicking “Create New Page” in the sidebar takes the user to a page where they can create a new encyclopedia entry. Users are able to enter a title for the page and, in a textarea, is able to enter the Markdown content for the page.
Users are able to click a button to save their new page.
When the page is saved, if an encyclopedia entry already exists with the provided title, the user will be presented with an error message.
Otherwise, the entry is saved to disk, and the user will be taken to the new entry’s page.


Edit Page: On each entry page, the user is able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a text area.
The text area will be pre-populated with the existing Markdown content of the page. (i.e., the existing content is the initial value of the textarea).
The user is able to click a button to save the changes made to the entry.
Once the entry is saved, the user is redirected back to that entry’s page.

Random Page: Clicking “Random Page” in the sidebar takes user to a random encyclopedia entry.
