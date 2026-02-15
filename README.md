# Trans Wellbeing Chatbot 🌈

An AI-powered mental health support chatbot specifically designed to provide compassionate, inclusive, and accessible emotional support for the transgender and gender-diverse community. Built with empathy, privacy, and evidence-based therapeutic approaches at its core.

## 🎯 Mission

To make mental health support radically accessible for transgender and gender-diverse individuals by providing a safe, judgment-free, and anonymous space for emotional wellbeing support, available 24/7.

## ✨ Features

- **24/7 Availability**: Access mental health support anytime, anywhere
- **Privacy-First**: Anonymous and confidential conversations
- **Evidence-Based**: Incorporates therapeutic techniques from CBT, mindfulness, and supportive counseling
- **Trans-Affirming**: Designed with understanding of transgender-specific mental health needs
- **Graph-Based Conversation Flow**: Intelligent state management for contextual, empathetic responses
- **No Login Required**: Immediate access without barriers

## 🏗️ Architecture

The chatbot is built using a modular, graph-based architecture for sophisticated conversation management:

```
Trans_wellbeing_chatbot/
│
├── app.py                    # Main Flask/Streamlit application
├── graph_builder.py          # Conversation flow and state management
├── state.py                  # State management and session handling
├── therapy_prompts.py        # Therapeutic prompts and response templates
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore configuration
└── .vscode/                 # VS Code settings
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Aishwary0402/Trans_wellbeing_chatbot.git
cd Trans_wellbeing_chatbot
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables** (if required)
```bash
# Create a .env file for API keys and configuration
cp .env.example .env  # Edit with your configuration
```

### Running the Application

```bash
python app.py
```

The chatbot will be accessible at `http://localhost:5000` (or the configured port).

## 📋 Requirements

Key dependencies (see `requirements.txt` for complete list):

- Flask/Streamlit - Web framework
- LangChain/LangGraph - Conversation flow management
- OpenAI/Anthropic API - Language model integration
- Python-dotenv - Environment variable management
- Additional NLP and ML libraries

## 🔧 Configuration

### Therapy Prompts

The `therapy_prompts.py` file contains:
- Empathetic response templates
- Crisis intervention protocols
- Trans-affirming language guidelines
- Cognitive behavioral therapy techniques
- Mindfulness and grounding exercises

### Graph Builder

The `graph_builder.py` module manages:
- Conversation state transitions
- Context-aware response generation
- Session memory management
- Therapeutic intervention triggers

### State Management

The `state.py` file handles:
- User session tracking
- Conversation history
- Emotional state monitoring
- Safety checks and escalation protocols

## 🌟 Key Capabilities

### Emotional Support
- Active listening and validation
- Empathetic responses
- Non-judgmental space
- Gender-affirming interactions

### Therapeutic Techniques
- **Cognitive Behavioral Therapy (CBT)**: Identify and reframe negative thought patterns
- **Mindfulness**: Grounding exercises and present-moment awareness
- **Dialectical Behavior Therapy (DBT)**: Emotion regulation and distress tolerance
- **Supportive Counseling**: Validation and coping strategies

### Trans-Specific Support
- Gender dysphoria coping strategies
- Coming out support
- Identity exploration
- Discrimination and minority stress management
- Transition-related emotional support

## 🛡️ Safety & Privacy

### Privacy Protection
- No personal data collection
- Anonymous conversations
- Encrypted communications
- No conversation storage (or minimal secure storage)
- GDPR/HIPAA compliance considerations

### Crisis Management
- Crisis detection protocols
- Emergency resource referrals
- Suicide prevention resources
- Professional help recommendations

### Limitations
⚠️ **Important**: This chatbot is NOT a replacement for professional mental health care. It is designed as a supportive tool and should not be used for:
- Psychiatric emergencies
- Diagnosis of mental health conditions
- Prescription of medication
- Treatment of severe mental illness

**In case of emergency, please contact:**
- National Suicide Prevention Lifeline: 988 (US)
- Trans Lifeline: 1-877-565-8860 (US)
- Local emergency services: 911 (US)
- Your local crisis helpline

## 🎨 User Experience

### Conversation Flow
1. Welcome and consent
2. Initial check-in
3. Identify support needs
4. Provide evidence-based interventions
5. Coping strategies and resources
6. Follow-up and closure

### Example Interactions
```
User: "I'm feeling really overwhelmed with my transition"
Bot: "I hear you, and it's completely valid to feel overwhelmed. Transition 
     is a significant journey with many emotional and practical challenges. 
     Would you like to talk about what's feeling most overwhelming right now?"

User: "I'm dealing with unsupportive family"
Bot: "That sounds incredibly difficult. Not having family support during 
     your journey can be very isolating. Remember that your identity is 
     valid regardless of others' acceptance. Let's explore some ways to 
     build support networks and coping strategies..."
```

## 🔬 Technical Details

### AI Model
- Large Language Model (LLM) integration
- Fine-tuned for empathetic responses
- Context-aware conversation management
- Safety filters and content moderation

### Graph-Based Architecture
- State machine for conversation flow
- Dynamic response generation
- Context preservation across sessions
- Intelligent routing based on user needs

## 🤝 Contributing

We welcome contributions from developers, mental health professionals, and community members!

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines

- Ensure trans-affirming and inclusive language
- Follow ethical AI development practices
- Test thoroughly for safety and appropriateness
- Document all changes clearly
- Respect user privacy and security

### Areas for Contribution
- [ ] Multilingual support
- [ ] Voice interface integration
- [ ] Mobile app development
- [ ] Additional therapeutic modalities
- [ ] Resource database expansion
- [ ] Accessibility improvements
- [ ] Community feedback integration

## 📚 Resources & References

### Mental Health Resources
- [Trans Lifeline](https://translifeline.org/)
- [The Trevor Project](https://www.thetrevorproject.org/)
- [PFLAG](https://pflag.org/)
- [WPATH - World Professional Association for Transgender Health](https://www.wpath.org/)

### Therapeutic Frameworks
- Cognitive Behavioral Therapy (CBT)
- Dialectical Behavior Therapy (DBT)
- Acceptance and Commitment Therapy (ACT)
- Trauma-Informed Care

### Technical References
- LangChain Documentation
- OpenAI API Documentation
- Mental Health Chatbot Best Practices
- AI Ethics in Healthcare

## 📊 Research & Validation

This chatbot is informed by:
- Evidence-based mental health practices
- Trans-affirming care principles
- User feedback and community input
- Clinical psychology research
- AI ethics and safety guidelines

## 🔮 Future Roadmap

### Short-term Goals
- Enhanced crisis detection
- Expanded resource database
- Multi-language support
- Mobile app release

### Long-term Vision
- Integration with professional therapist networks
- Community peer support features
- Personalized therapeutic plans
- Research partnerships with mental health organizations
- Outcome measurement and effectiveness studies

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Aishwary0402**
- GitHub: [@Aishwary0402](https://github.com/Aishwary0402)

## 🙏 Acknowledgments

- Mental health professionals who reviewed the therapeutic content
- Transgender community members who provided feedback
- Open-source AI and NLP communities
- Organizations dedicated to trans mental health support

## 💬 Feedback & Support

We value your feedback! If you have:
- **Bug Reports**: Open an issue with the `bug` label
- **Feature Requests**: Open an issue with the `enhancement` label
- **Questions**: Start a discussion in the Discussions tab
- **Security Concerns**: Please email privately (see SECURITY.md)

## ⚠️ Disclaimer

This chatbot provides emotional support and coping strategies based on evidence-based therapeutic techniques. It is NOT a substitute for professional mental health care, diagnosis, or treatment. If you are experiencing a mental health crisis, please seek immediate help from qualified healthcare professionals or emergency services.

The information provided by this chatbot is for educational and supportive purposes only and should not be considered medical advice.

---

**Remember**: You are valid. You deserve support. You are not alone. 🌈💙💗🤍💗💙
