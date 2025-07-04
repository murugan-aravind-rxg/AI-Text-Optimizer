#AI-Text-Optimizer...using Groq...

# llm based response generator.
def generate_llm_response(provider, system_msg, user_msg, temperature=0.7):
    if provider == "groq":
        from openai import OpenAI
        client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )
        model = "llama-3.3-70b-versatile"
    elif provider == "openai":
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        model = "gpt-4"
    else:
        raise ValueError(f"Unsupported provider: {provider}")

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

# llm based text optimier
def llm_optimizer(provider, prompt, feedback=None):
    system_msg = "You are a helpful assistant that refines text based on evaluator feedback."
    user_msg = prompt if not feedback else f"Refine this text to address the feedback: '{feedback}'\n\nText:\n{prompt}"
    return generate_llm_response(provider, system_msg, user_msg, temperature=0.7)

# llm based text feedback provider
def llm_evaluator(provider, prompt, response):
    """
    Evaluate the quality of an LLM response using another LLM as a judge.
    
    This function uses a separate LLM with temperature=0 (deterministic) to ensure
    consistent evaluation results for the same input.
    
    Args:
        provider: LLM provider ("groq" or "openai")
        prompt: The original prompt that was given to the LLM
        response: The LLM response to evaluate
    
    Returns:
        tuple: (is_accepted, feedback)
            - is_accepted: Boolean indicating if response meets quality threshold
            - feedback: Detailed feedback if not accepted, None if accepted
    """
    # Define the evaluator's role and evaluation criteria
    evaluator_system_message = "You are a strict evaluator judging the quality of LLM outputs."
    
    # Create the evaluation prompt with clear instructions
    evaluation_prompt = (
        f"Evaluate the following response to the prompt. "
        f"Score it 0–1. If under 0.7, explain what must be improved.\n\n"
        f"Prompt: {prompt}\n\nResponse: {response}"
    )
    
    # Get evaluation from LLM with temperature=0 for consistency
    evaluation_result = generate_llm_response(provider, evaluator_system_message, evaluation_prompt, temperature=0)
    
    # Parse the evaluation score
    # Look for explicit score mentions in the response
    has_acceptable_score = "Score: 0.7" in evaluation_result or "Score: 1" in evaluation_result
    quality_score = 1.0 if has_acceptable_score else 0.5
    
    # Determine if response meets quality threshold
    is_accepted = quality_score >= 0.7
    
    # Return appropriate feedback based on acceptance
    feedback = None if is_accepted else evaluation_result
    
    return is_accepted, feedback


# optimizer Text generation
def optimize_prompt(prompt, provider="groq", max_iterations=5):
    """
    Iteratively optimize a prompt using LLM feedback loop.
    
    This function implements a feedback loop where:
    1. An LLM optimizer generates an improved version of the text
    2. An LLM evaluator assesses the quality of the improved version
    3. If accepted, the process stops; if not, the feedback is used for the next iteration
    
    Args:
        prompt: The original text to optimize
        provider: LLM provider ("groq" or "openai")
        max_iterations: Maximum number of optimization attempts
    
    Returns:
        The optimized text or the best version after max iterations
    """
    current_text = prompt
    previous_feedback = None
    
    for iteration in range(max_iterations):
        print(f"\n🔄 Iteration {iteration + 1}")
        
        # Step 1: Generate optimized version based on current text and feedback
        optimized_text = llm_optimizer(provider, current_text, previous_feedback)
        print(f"🧠 Optimized: {optimized_text}\n")
        
        # Step 2: Evaluate the optimized version
        is_accepted, evaluation_feedback = llm_evaluator(provider, prompt, optimized_text)
        
        if is_accepted:
            print("✅ Accepted by evaluator")
            return optimized_text
        else:
            print(f"❌ Feedback: {evaluation_feedback}\n")
            # Step 3: Prepare for next iteration
            current_text = optimized_text
            previous_feedback = evaluation_feedback

    print("⚠️ Max iterations reached.")
    return current_text

if __name__ == "__main__":
    prompt = "Summarize the key points of Next.js payload compression strategies."
    final_output = optimize_prompt(prompt, provider="groq")
    print(f"\n🎯 Final Output:\n{final_output}")

