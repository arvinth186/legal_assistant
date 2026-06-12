from legalassistant.crew import LegalAssistant


def run():
    inputs = {
        "user_input": """
        A man broke into my house at night while my family was sleeping.
        He stole jewelry and cash from our bedroom.
        When I confronted him, he threatened me with a knife and ran away.
        """
    }

    result = LegalAssistant().crew().kickoff(inputs=inputs)

    print("\n")
    print("=" * 80)
    print(result)
    print("=" * 80)


if __name__ == "__main__":
    run()
    
    