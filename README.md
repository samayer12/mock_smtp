**Dramatis Personae:**

- `send_email()` <- Unit test target
- `build_email()` <- Used by send_email()
- `smtplib` <- External library we are confident in
- `ssl` <- External library we are confident in

Our unit test should only check the behavior of what `send_email()` brings to the party. 
In this case: logon, storing the transmission result (I'm not familiar with that looks like offhand), and logoff.

- Create a stub for `build_email` as we don't want to actually invoke it. I mean, it's fine, but now our unit test is technically functional test (which also have their place).
- I prefer patch annotations for the sake of clarity, I don't think we really need a context manager here, but that's fine.
- Specify the return value of `build_email`, this ensures that you explicitly state what a "good" email is for your system.
- We care that we establish an SMTP over SSL session with `smtp.gmail.com` on port 465. That's good to have baked into your test (self-documenting!).
- We also care that SMTP session creation and teardown happens. We do that with the assertions on `spy_result`.
- Shameless plug for the [talk I gave](https://www.youtube.com/watch?v=h75UJmzXz6k) on mocks from awhile back. 