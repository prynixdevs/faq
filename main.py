import streamlit as st

st.set_page_config(
    page_title="Prynix FAQ",
    page_icon="❓",
    layout="centered"
)

st.markdown("""
<style>
/* FAQ question text */
[data-testid="stExpander"] summary p {
    font-size: 1.2rem !important;
    font-weight: 600 !important;
}

/* FAQ answer text */
[data-testid="stExpander"] .stMarkdown p {
    font-size: 1.05rem !important;
    line-height: 1.6 !important;
}

/* Add a little spacing between FAQs */
[data-testid="stExpander"] {
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)


st.title("Prynix FAQ")

st.write(
    "Frequently Asked Questions about Prynix"
)


faqs = [
    (
        "What is Prynix?",
        """Prynix is a community of teen developers based in Nepal who learn
and build software and game projects together. It is not a company or a
product. It is a group of people."""
    ),

    (
        "What does Prynix do?",
        """Members, called "Prynix Devs", build real projects together,
including websites, games, and tools like a Discord bot. They also take
part in hackathons and game jams as a group."""
    ),

    (
        "What problem does Prynix solve?",
        """Prynix gives student developers a place to actually build things
with other people instead of learning alone. Many young developers know
how to code but do not have a community around them to build real projects
with, get feedback from, or team up with for events like hackathons."""
    ),

    (
        "How does Prynix work?",
        """There is no formal company structure. Prasoon Kandel leads Prynix
as Founder, with Pratik Chalise and Aayush Parajuli as founding members.
Beyond that, it is community-driven."""
    ),

    (
        "What has Prynix accomplished so far?",
        """Prynix is still a young, small community founded in mid-2025.
Its members have built and shipped real projects together. One example is
Corpse Climber, a Unity puzzle-platformer that placed 2nd in the theming
category at the Daydream Global game jam."""
    ),

    (
        "Why does Prynix exist, and who is it for?",
        """Prynix exists because its founders wanted a real community where
student developers could build things together instead of just talking
about code. It is for teen and student developers, from beginners to
experienced coders."""
    ),

    (
        "Is Prynix a company or a startup?",
        """No. Prynix is a community of teen developers in Nepal who build
projects together. It is not a business and does not have investors,
employees, or a product it sells."""
    ),

    (
        "Who is actually in charge of Prynix?",
        """Prasoon Kandel is the Founder and Lead. Pratik Chalise and
Aayush Parajuli are Founding Members, with roles as Co-Lead and Technical
Lead respectively.

They are not co-founders. Only Prasoon founded Prynix."""
    ),

    (
        'Is Aayush and "Hexagrim" the same person?',
        """Yes. Hexagrim is Aayush Parajuli's online handle, which he uses
on platforms such as itch.io and GitHub."""
    ),

    (
        'What is a "Prynix Dev"?',
        """A Prynix Dev is simply a member of the Prynix community. You do
not need to be a professional coder to be one. Beginners count too."""
    ),

    (
        "Does joining the Discord make me an official Prynix member?",
        """No. Joining the Discord server lets you hang out and chat with
the community. To become an official Prynix Dev, you need to fill out the
actual application form."""
    ),

    (
        "Does Prynix cost money to join?",
        """No. Official Prynix membership is free."""
    ),

    (
        "Where do I apply?",
        """You can apply here:

https://prynix.fillout.com/apply"""
    ),

    (
        "Is Prynix Hack Club the same thing as Prynix?",
        """No.

Prynix Hack Club is a smaller and separate local club connected to the
global Hack Club network. It is casually run by a handful of Prynix
developers from Butwal.

It is not the whole of Prynix."""
    ),

    (
        "If Prynix Hack Club membership is closed, does that mean Prynix itself is closed too?",
        """No. They are two separate memberships.

If Hack Club membership is closed, that does not affect whether you can
apply to become a regular Prynix Dev. The Prynix application is separate."""
    ),

    (
        "Is Prynix only for people who already know how to code?",
        """There is no publicly stated requirement that you already know
how to code to join Prynix. Beginners are welcome."""
    ),

    (
        "Is Prynix only for people in Nepal or Butwal?",
        """No. People outside Nepal can also be part of the Prynix community.

Prynix itself is based in Nepal, while the Prynix Hack Club group is
specifically made up of developers from Butwal."""
    ),

    (
        "What does Prynix actually build?",
        """Prynix members mainly build student-driven projects such as
websites, games, Discord bots, and other tools.

They also participate in hackathons and game jams as a community."""
    ),

    (
        "How is Prynix different from just joining a regular Hack Club chapter?",
        """Prynix is its own independent community with its own projects,
Discord server, and membership.

Prynix Hack Club is a locally run club affiliated with the global Hack
Club network, but it is not what Prynix itself is."""
    ),
]


for question, answer in faqs:
    with st.expander(question):
        st.write(answer)
